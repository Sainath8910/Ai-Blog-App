"""
Base Google AI Provider.

Every Google provider (Gemini, Imagen, Gemini Image, etc.)
inherits from this class.
"""

from google import genai

from ai_pipeline.config.settings import GEMINI_API_KEY

from ai_pipeline.utils.logger import logger


class GoogleProvider:
    """
    Base class for all Google AI providers.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        logger.info(
            "Google client initialized."
        )