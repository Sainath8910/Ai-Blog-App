"""
Schema validation using Pydantic models.
"""

from pydantic import ValidationError

from ai_pipeline.models.blog import Blog


class SchemaValidator:
    """
    Validates the generated blog JSON against the Blog model.
    """

    @staticmethod
    def validate(json_text: str) -> Blog:
        """
        Validate JSON and return a Blog object.

        Args:
            json_text: JSON returned by the LLM.

        Returns:
            Blog object.

        Raises:
            ValidationError
        """

        return Blog.model_validate_json(json_text)