"""
OpenRouter LLM Provider.
"""

import requests

from ai_pipeline.config.settings import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    OPENROUTER_MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
)

from ai_pipeline.providers.base.llm_provider import LLMProvider

from ai_pipeline.utils.logger import logger


class OpenRouterProvider(LLMProvider):
    """
    OpenRouter implementation.
    """

    @property
    def name(self) -> str:
        return "OpenRouter"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float | None = None,
        max_output_tokens: int | None = None,
    ) -> str:

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            "temperature": (
                temperature
                if temperature is not None
                else TEMPERATURE
            ),
            "max_tokens": (
                max_output_tokens
                if max_output_tokens is not None
                else MAX_OUTPUT_TOKENS
            ),
        }

        response = requests.post(
            OPENROUTER_BASE_URL,
            headers=headers,
            json=payload,
            timeout=180,
        )

        response.raise_for_status()

        data = response.json()

        logger.info(
            "OpenRouter response generated successfully."
        )

        return data["choices"][0]["message"]["content"]