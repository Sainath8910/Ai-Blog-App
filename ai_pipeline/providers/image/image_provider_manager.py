"""
Image Provider Manager.
"""

import time

from ai_pipeline.config.settings import (
    IMAGE_PRIMARY_PROVIDER,
    IMAGE_BACKUP_PROVIDERS,
)

from ai_pipeline.providers.image.pollinations_provider import PollinationsProvider

from ai_pipeline.utils.logger import logger
from ai_pipeline.providers.image.pollinations_flux_dev_provider import PollinationsFluxDevProvider

from ai_pipeline.providers.image.pollinations_turbo_provider import PollinationsTurboProvider
from ai_pipeline.providers.image.cloudflare_dreamshaper_provider import CloudflareDreamShaperProvider
from ai_pipeline.providers.image.cloudflare_sdxl_provider import CloudflareSDXLProvider
class ImageProviderManager:

    def __init__(self):

        self.registry = {
            "cloudflare_dreamshaper": CloudflareDreamShaperProvider(),
            "cloudflare_sdxl": CloudflareSDXLProvider(),

            "pollinations": PollinationsProvider(),
            "pollinations_flux_dev": PollinationsFluxDevProvider(),
            "pollinations_turbo": PollinationsTurboProvider(),
        }

        self.providers = [
            IMAGE_PRIMARY_PROVIDER,
            *IMAGE_BACKUP_PROVIDERS,
        ]

        self.max_retries = 2

    def generate(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 1024,
    ) -> bytes:

        last_exception = None

        for provider_name in self.providers:

            provider = self.registry[provider_name]

            logger.info(
                "Using image provider: %s",
                provider.name,
            )

            for attempt in range(self.max_retries + 1):

                try:

                    return provider.generate(
                        prompt=prompt,
                        width=width,
                        height=height,
                    )

                except Exception as e:

                    logger.warning(
                        "%s failed (%s)",
                        provider.name,
                        e,
                    )

                    last_exception = e

                    if attempt < self.max_retries:

                        wait = 2 ** attempt

                        logger.info(
                            "Retrying in %s seconds...",
                            wait,
                        )

                        time.sleep(wait)

            logger.info("Switching provider...")

        raise RuntimeError(
            f"All image providers failed.\n\n{last_exception}"
        )