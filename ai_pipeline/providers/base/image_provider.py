"""
Base interface for all image providers.
"""

from abc import ABC
from abc import abstractmethod


class ImageProvider(ABC):
    """
    Abstract base class for all image generation providers.
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
        prompt: str,
        width: int = 1024,
        height: int = 1024,
    ) -> bytes:
        """
        Generate an image.

        Returns:
            Raw image bytes.
        """
        raise NotImplementedError