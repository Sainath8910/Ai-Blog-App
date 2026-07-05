from pydantic import BaseModel
from django.db import transaction
from django.db.models import Q

from blogs.models import Blog
from blogs.repositories.chapter_repository import ChapterRepository


def serialize(value):
    """
    Recursively convert Pydantic models into
    plain Python objects that Django JSONField
    can store.
    """

    if value is None:
        return None

    if isinstance(value, BaseModel):
        return value.model_dump()

    if isinstance(value, list):
        return [serialize(item) for item in value]

    if isinstance(value, dict):
        return {
            key: serialize(val)
            for key, val in value.items()
        }

    return value


class BlogRepository:

    @staticmethod
    @transaction.atomic
    def create_blog(
        blog,
        user_id,
        generation_uuid,
    ):
        """
        Save a generated blog and all its chapters.
        """

        db_blog = Blog.objects.create(

            # ------------------------------------
            # Blog Info
            # ------------------------------------

            user_id=user_id,
            generation_uuid=generation_uuid,
            topic=blog.blog_info.topic,
            language=blog.blog_info.language,
            tone=blog.blog_info.tone,
            blog_type=blog.blog_info.blog_type,
            target_audience=blog.blog_info.target_audience,

            # ------------------------------------
            # Metadata
            # ------------------------------------

            title=blog.metadata.title,
            slug=blog.metadata.slug,
            description=blog.metadata.description,
            category=blog.metadata.category,
            keywords=serialize(blog.metadata.keywords),
            tags=serialize(blog.metadata.tags),

            # ------------------------------------
            # Rich Content
            # ------------------------------------

            hero=serialize(blog.hero),

            key_takeaways=serialize(
                blog.key_takeaways
            ),

            faq=serialize(
                blog.faq
            ),

            resources=serialize(
                blog.resources
            ),

            call_to_action=serialize(
                blog.call_to_action
            ),

            conclusion=serialize(
                blog.conclusion
            ),

            # ------------------------------------
            # Generation
            # ------------------------------------

            processing_status="completed",

            status="draft",

            llm_provider="gemini",

            image_provider="pollinations",

        )

        ChapterRepository.bulk_create(
            db_blog,
            blog.chapters,
        )

        return db_blog

    @staticmethod
    def get_blog(blog_id):

        return Blog.objects.prefetch_related(
            "chapters"
        ).get(
            id=blog_id,
            is_deleted=False,
        )

    
    @staticmethod
    def get_user_blogs(
        user_id,
        search="",
        category="",
        status="",
    ):

        blogs = Blog.objects.filter(
            user_id=user_id,
            is_deleted=False,
        )

        if search:

            blogs = blogs.filter(

                Q(title__icontains=search) |

                Q(topic__icontains=search) |

                Q(description__icontains=search)

            )

        if category:

            blogs = blogs.filter(
                category=category
            )

        if status:

            blogs = blogs.filter(
                status=status
            )

        return blogs.order_by("-created_at")

    @staticmethod
    @transaction.atomic
    def update_blog(blog, data):

        # -----------------------------
        # Metadata
        # -----------------------------

        blog.title = data["title"]

        blog.description = data["description"]

        blog.category = data["category"]

        blog.language = data["language"]

        blog.tone = data["tone"]

        blog.target_audience = data["target_audience"]

        blog.status = data["status"]

        blog.save()

        # -----------------------------
        # Chapters
        # -----------------------------

        for chapter_data in data["chapters"]:

            chapter = blog.chapters.get(

                id=chapter_data["id"]

            )

            chapter.title = chapter_data["title"]

            chapter.paragraphs = chapter_data["paragraphs"]

            chapter.bullet_points = chapter_data["bullet_points"]

            chapter.save()

        return blog

    @staticmethod
    def delete_blog(blog):

        blog.is_deleted = True

        blog.save(
            update_fields=["is_deleted"]
        )

    @staticmethod
    def save(blog):

        blog.save()

        return blog