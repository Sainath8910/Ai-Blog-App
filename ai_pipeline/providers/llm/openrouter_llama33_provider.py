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


class OpenRouterLlama33Provider(LLMProvider):
    """
    OpenRouter implementation.
    """
    MODEL =  "meta-llama/llama-3.3-70b-instruct"
    @property
    def name(self) -> str:
        return "OpenRouter - Llama 3.3 70B"

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
            "model": self.MODEL,
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
            "%s response generated successfully.",self.name,
        )

        return data["choices"][0]["message"]["content"]