from ai_pipeline.pipeline.image_pipeline import ImagePipeline
from blogs.services.storage_service import StorageService


class ImageService:

    def __init__(self):

        self.pipeline = ImagePipeline()

        self.storage = StorageService()

    def generate_images(

        self,

        blog,

        user_id,

        generation_uuid,

    ):

        """
        Generate all images, upload them to Supabase,
        then update the blog with public URLs.
        """

        generated_images = self.pipeline.generate(blog)

        # ------------------------------------------
        # Hero
        # ------------------------------------------

        stored = self.storage.upload_image(

            image=generated_images["hero"],

            user_id=user_id,

            generation_uuid=str(generation_uuid),

            image_name="hero",

        )

        blog.hero.image.path = stored.public_url

        # ------------------------------------------
        # Chapters
        # ------------------------------------------

        for index, chapter in enumerate(blog.chapters):

            stored = self.storage.upload_image(

                image=generated_images["chapters"][index],

                user_id=user_id,

                generation_uuid=str(generation_uuid),

                image_name=f"chapter_{chapter.id}",

            )

            chapter.image.path = stored.public_url

        # ------------------------------------------
        # Conclusion
        # ------------------------------------------

        stored = self.storage.upload_image(

            image=generated_images["conclusion"],

            user_id=user_id,

            generation_uuid=str(generation_uuid),

            image_name="conclusion",

        )

        blog.conclusion.image.path = stored.public_url

        return blog