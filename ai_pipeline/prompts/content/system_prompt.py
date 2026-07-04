"""
Loads the Content Agent system prompt.

The prompt itself is stored in system_prompt.txt to keep
the Python code clean and make prompt editing easier.
"""

from pathlib import Path

PROMPT_FILE = Path(__file__).parent / "system_prompt.txt"

CONTENT_SYSTEM_PROMPT = PROMPT_FILE.read_text(
    encoding="utf-8"
)