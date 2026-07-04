from django.db import transaction

from blogs.models import BlogChapter
from blogs.utils.serializer import serialize


class ChapterRepository:
    """
    Handles all BlogChapter database operations.
    """

    @staticmethod
    @transaction.atomic
    def bulk_create(
        blog,
        chapters,
    ):
        """
        Create all chapters for a blog in one query.
        """

        objects = []

        for chapter in chapters:

            objects.append(

                BlogChapter(

                    blog=blog,

                    order=chapter.id,

                    purpose=chapter.purpose,

                    title=chapter.title,

                    paragraphs=serialize(
                        chapter.paragraphs
                    ),

                    bullet_points=serialize(
                        chapter.bullet_points
                    ),

                    numbered_steps=serialize(
                        chapter.numbered_steps
                    ),

                    tips=serialize(
                        chapter.tips
                    ),

                    warnings=serialize(
                        chapter.warnings
                    ),

                    notes=serialize(
                        chapter.notes
                    ),

                    examples=serialize(
                        chapter.examples
                    ),

                    quotes=serialize(
                        chapter.quotes
                    ),

                    code_examples=serialize(
                        chapter.code_examples
                    ),

                    tables=serialize(
                        chapter.tables
                    ),

                    image=serialize(
                        chapter.image
                    ),

                )

            )

        return BlogChapter.objects.bulk_create(
            objects
        )

    @staticmethod
    def get_chapters(blog):

        return BlogChapter.objects.filter(
            blog=blog
        ).order_by("order")

    @staticmethod
    def get_chapter(
        blog,
        order,
    ):

        return BlogChapter.objects.get(
            blog=blog,
            order=order,
        )

    @staticmethod
    def update_chapter(
        chapter,
        **kwargs,
    ):
        """
        Update only the supplied fields.
        """

        for key, value in kwargs.items():

            setattr(
                chapter,
                key,
                serialize(value),
            )

        chapter.save()

        return chapter

    @staticmethod
    def delete_chapter(
        chapter,
    ):

        chapter.delete()

    @staticmethod
    def delete_all(
        blog,
    ):

        BlogChapter.objects.filter(
            blog=blog
        ).delete()