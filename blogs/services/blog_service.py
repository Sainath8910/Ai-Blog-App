import time
import uuid

from ai_pipeline.pipeline.blog_pipeline import BlogPipeline
from ai_pipeline.models.blog_request import BlogRequest

from blogs.repositories.blog_repository import BlogRepository
from blogs.services.image_service import ImageService


class BlogService:
    """
    Orchestrates the complete blog generation workflow.
    """

    def __init__(self):

        self.pipeline = BlogPipeline()

        self.image_service = ImageService()

        self.repository = BlogRepository()

    def generate(
        self,
        request: BlogRequest,
        user_id: str,
    ):

        generation_uuid = uuid.uuid4()

        start = time.perf_counter()

        # Generate blog content
        blog = self.pipeline.generate(request)

        # Generate images and upload to Supabase
        blog = self.image_service.generate_images(
            blog=blog,
            user_id=user_id,
            generation_uuid=generation_uuid,
        )

        end = time.perf_counter()

        # Save everything
        db_blog = self.repository.create_blog(
            blog=blog,
            user_id=user_id,
            generation_uuid=generation_uuid,
        )

        db_blog.generation_time = round(end - start, 2)

        db_blog.save(update_fields=["generation_time"])

        return db_blog