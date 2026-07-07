from ai_pipeline.models.blog_request import BlogRequest

from blogs.services.blog_service import BlogService
from blogs.repositories.blog_repository import BlogRepository


class BlogRegenerationService:
    """
    Regenerates an existing blog while preserving its ID.
    """

    def __init__(self):

        self.blog_service = BlogService()

        self.repository = BlogRepository()

    def regenerate(
        self,
        blog,
    ):

        request = BlogRequest(
            topic=blog.topic,
            content_brief=blog.description,
            target_audience=blog.target_audience,
            tone=blog.tone,
            length=blog.length,
            keywords=blog.keywords,
        )

        generated_blog = self.blog_service.generate_content(

            request=request,

            user_id=str(blog.user_id),

            generation_uuid=blog.generation_uuid,

        )

        updated_blog = self.repository.replace_blog(

            existing_blog=blog,

            generated_blog=generated_blog,

        )

        return updated_blog