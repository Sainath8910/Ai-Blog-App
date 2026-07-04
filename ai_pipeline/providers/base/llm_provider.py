"""
Base interface for all LLM providers.
"""

from abc import ABC
from abc import abstractmethod


class LLMProvider(ABC):
    """
    Abstract base class for all text generation providers.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Provider name.
        """
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float | None = None,
        max_output_tokens: int | None = None,
    ) -> str:
        """
        Generate text response.
        """
        raise NotImplementedError