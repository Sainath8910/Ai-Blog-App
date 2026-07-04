"""
Main blog generation pipeline.
"""

import json

from ai_pipeline.models.blog import Blog
from ai_pipeline.models.blog_request import BlogRequest

from ai_pipeline.prompts.content.system_prompt import CONTENT_SYSTEM_PROMPT
from ai_pipeline.prompts.content.user_prompt import build_user_prompt

from ai_pipeline.providers.llm.llm_manager import LLMManager

from ai_pipeline.validators.schema_validator import SchemaValidator
from ai_pipeline.utils.normalizer import BlogNormalizer
from ai_pipeline.utils.json_utils import JSONUtils
from ai_pipeline.utils.logger import logger


class BlogPipeline:
    """
    Coordinates the complete blog generation workflow.
    """

    def __init__(self) -> None:

        self.provider = LLMManager()
        self.validator = SchemaValidator()

    def generate(
        self,
        request: BlogRequest,
    ) -> Blog:
        """
        Generate a validated Blog object.
        """

        logger.info(
            "Generating blog for topic: %s",
            request.topic
        )

        user_prompt = build_user_prompt(request)

        raw_response = self.provider.generate(
            system_prompt=CONTENT_SYSTEM_PROMPT,
            user_prompt=user_prompt,
        )

        clean_json = JSONUtils.extract_json(raw_response)

        clean_json = JSONUtils.validate_json(clean_json)
        blog_dict = json.loads(clean_json)

        blog_dict = BlogNormalizer.normalize(blog_dict)

        clean_json = json.dumps(
            blog_dict,
            ensure_ascii=False,
        )
        blog = self.validator.validate(clean_json)

        logger.info(
            "Blog validated successfully."
        )

        return blog