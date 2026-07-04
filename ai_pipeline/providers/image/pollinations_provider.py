"""
Pollinations Image Provider.
"""

import requests

from ai_pipeline.providers.base.image_provider import ImageProvider

from ai_pipeline.utils.logger import logger


class PollinationsProvider(ImageProvider):
    """
    Free image generation using Pollinations.
    """

    BASE_URL = "https://image.pollinations.ai/prompt/"

    @property
    def name(self) -> str:
        return "Pollinations"

    def generate(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 1024,
    ) -> bytes:

        response = requests.get(
            self.BASE_URL + prompt,
            timeout=180,
        )

        response.raise_for_status()

        logger.info(
            "Image generated using Pollinations."
        )

        return response.content