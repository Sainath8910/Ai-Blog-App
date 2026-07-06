"""
Cloudflare Workers AI Image Provider.
"""

import requests

from ai_pipeline.config.settings import (
    CLOUDFLARE_API_TOKEN,
    CLOUDFLARE_ACCOUNT_ID,
)

from ai_pipeline.providers.base.image_provider import ImageProvider

from ai_pipeline.utils.logger import logger


class CloudflareDreamShaperProvider(ImageProvider):
    """
    Cloudflare Workers AI FLUX image generation provider.
    """

    MODEL = "@cf/lykon/dreamshaper-8-lcm"

    @property
    def name(self) -> str:
        return "Cloudflare - DreamShaper 8"

    def generate(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 1024,
    ) -> bytes:

        
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/"
            f"{CLOUDFLARE_ACCOUNT_ID}/ai/run/{self.MODEL}"
        )

        headers = {
            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "prompt": prompt,
            "width": width,
            "height": height,
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        logger.info(
            "%s image generated successfully.",
            self.name,
        )

        return response.content