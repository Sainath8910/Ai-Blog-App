from ai_pipeline.models.generated_image import GeneratedImage

from ai_pipeline.providers.image.image_provider_manager import (
    ImageProviderManager,
)


class ImageGenerator:

    def __init__(self):

        self.provider = ImageProviderManager()

    def generate(
        self,
        prompt: str,
        alt_text: str = "",
    ) -> GeneratedImage:

        image_bytes = self.provider.generate(prompt)

        return GeneratedImage(

            image_bytes=image_bytes,

            prompt=prompt,

            alt_text=alt_text,

            extension=".png",

            mime_type="image/png",

            provider="pollinations",

        )