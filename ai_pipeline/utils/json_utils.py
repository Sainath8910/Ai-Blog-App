"""
Utilities for extracting and validating JSON returned by LLMs.
"""

import json
import re


class JSONUtils:
    """Utility methods for handling JSON responses."""

    @staticmethod
    def extract_json(text: str) -> str:
        """
        Extract JSON from an LLM response.
        """

        text = text.strip()

        # Remove markdown code fences
        text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"```$", "", text)

        # Find first opening brace
        start = text.find("{")

        if start == -1:
            raise ValueError("No JSON object found.")

        # Find last closing brace
        end = text.rfind("}")

        if end == -1:
            raise ValueError("JSON appears incomplete.")

        return text[start:end + 1]

    @staticmethod
    def validate_json(text: str) -> str:
        """
        Ensure extracted JSON is valid.
        """

        json.loads(text)

        return text