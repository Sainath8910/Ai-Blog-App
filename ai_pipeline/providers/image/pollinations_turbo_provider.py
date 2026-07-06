"""
Pollinations Image Provider.
"""

import requests

from ai_pipeline.providers.base.image_provider import ImageProvider

from ai_pipeline.utils.logger import logger
import urllib.parse

class PollinationsTurboProvider(ImageProvider):
    """
    Free image generation using Pollinations.
    """

    BASE_URL = "https://image.pollinations.ai/prompt/"

    @property
    def name(self) -> str:
        return "Pollinations - Turbo"

    def generate(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 1024,
    ) -> bytes:

        encoded_prompt = urllib.parse.quote(prompt)

        response = requests.get(
            f"{self.BASE_URL}{encoded_prompt}",
            params={
                "model": "turbo",
                "width": width,
                "height": height,
            },
            timeout=180,
        )

        response.raise_for_status()

        logger.info(
            "Image generated using Pollinations."
        )

        return response.content