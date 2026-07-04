"""
Gemini LLM Provider.
"""

from google.genai.types import GenerateContentConfig
from google.genai.types import Part
from google.genai.types import Content

from ai_pipeline.config.settings import (
    CONTENT_MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
)

from ai_pipeline.providers.base.google_provider import GoogleProvider
from ai_pipeline.providers.base.llm_provider import LLMProvider

from ai_pipeline.utils.logger import logger


class GeminiProvider(GoogleProvider, LLMProvider):
    """
    Gemini text generation provider.
    """

    @property
    def name(self) -> str:
        return "Gemini 2.5 Flash"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float | None = None,
        max_output_tokens: int | None = None,
    ) -> str:

        response = self.client.models.generate_content(

            model=CONTENT_MODEL,

            contents=[
                Content(
                    role="user",
                    parts=[
                        Part.from_text(
                            text=user_prompt
                        )
                    ],
                )
            ],

            config=GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=(
                    temperature
                    if temperature is not None
                    else TEMPERATURE
                ),
                max_output_tokens=(
                    max_output_tokens
                    if max_output_tokens is not None
                    else MAX_OUTPUT_TOKENS
                ),
            ),
        )

        logger.info(
            "Gemini response generated successfully."
        )

        return response.text