"""
LLM Provider Manager.

Responsible for:
- Provider selection
- Retry
- Automatic fallback
"""

import time

from ai_pipeline.config.settings import (
    PRIMARY_LLM,
    BACKUP_LLMS,
)

from ai_pipeline.providers.llm.gemini_provider import GeminiProvider
from ai_pipeline.providers.llm.openrouter_provider import OpenRouterProvider

from ai_pipeline.utils.logger import logger


class LLMManager:

    def __init__(self):

        self.registry = {
            "gemini": GeminiProvider(),
            "openrouter": OpenRouterProvider(),
        }

        self.providers = [
            PRIMARY_LLM,
            *BACKUP_LLMS,
        ]

        self.max_retries = 2

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float | None = None,
        max_output_tokens: int | None = None,
    ) -> str:

        last_exception = None

        for provider_name in self.providers:

            provider = self.registry[provider_name]

            logger.info(
                "Using provider: %s",
                provider.name,
            )

            for attempt in range(self.max_retries + 1):

                try:

                    if attempt:

                        logger.info(
                            "Retry %s (%s)",
                            attempt,
                            provider.name,
                        )

                    return provider.generate(
                        system_prompt=system_prompt,
                        user_prompt=user_prompt,
                        temperature=temperature,
                        max_output_tokens=max_output_tokens,
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
                            "Waiting %s seconds...",
                            wait,
                        )

                        time.sleep(wait)

            logger.info(
                "Switching provider..."
            )

        raise RuntimeError(
            f"All LLM providers failed.\n\n{last_exception}"
        )