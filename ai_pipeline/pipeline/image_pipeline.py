"""
Image generation pipeline.
"""

from ai_pipeline.models.blog import Blog
from ai_pipeline.pipeline.image_generator import ImageGenerator
from ai_pipeline.utils.logger import logger


class ImagePipeline:
    """
    Generates all images for a blog.

    Returns GeneratedImage objects.
    """

    def __init__(self):
        self.generator = ImageGenerator()

    def generate(self, blog: Blog) -> dict:
        """
        Generate all images.

        Returns a dictionary of GeneratedImage objects.
        """

        logger.info("Generating hero image...")

        images = {
            "hero": self.generator.generate(
                prompt=blog.hero.image.prompt,
                alt_text=blog.hero.image.alt_text,
            ),
            "chapters": [],
            "conclusion": None,
        }

        for chapter in blog.chapters:

            logger.info(
                "Generating image for Chapter %s",
                chapter.id,
            )

            images["chapters"].append(
                self.generator.generate(
                    prompt=chapter.image.prompt,
                    alt_text=chapter.image.alt_text,
                )
            )

        logger.info("Generating conclusion image...")

        images["conclusion"] = self.generator.generate(
            prompt=blog.conclusion.image.prompt,
            alt_text=blog.conclusion.image.alt_text,
        )

        logger.info("Image generation completed.")

        return images