"""
Normalizes LLM JSON output before Pydantic validation.
"""

from copy import deepcopy


class BlogNormalizer:

    @staticmethod
    def normalize(blog: dict) -> dict:

        blog = deepcopy(blog)

        chapters = blog.get("chapters", [])

        for chapter in chapters:

            BlogNormalizer._normalize_numbered_steps(chapter)

            BlogNormalizer._normalize_examples(chapter)

            BlogNormalizer._normalize_quotes(chapter)

            BlogNormalizer._normalize_code_examples(chapter)

            BlogNormalizer._normalize_tables(chapter)

        return blog

    # -------------------------------------------------

    @staticmethod
    def _normalize_numbered_steps(chapter):

        steps = chapter.get("numbered_steps", [])

        normalized = []

        for index, step in enumerate(steps, start=1):

            if isinstance(step, str):

                normalized.append(
                    {
                        "title": f"Step {index}",
                        "description": step
                    }
                )

            else:

                normalized.append(step)

        chapter["numbered_steps"] = normalized

    # -------------------------------------------------

    @staticmethod
    def _normalize_examples(chapter):

        examples = chapter.get("examples", [])

        normalized = []

        for example in examples:

            if isinstance(example, str):

                normalized.append(
                    {
                        "title": "Example",
                        "description": example
                    }
                )

            else:

                normalized.append(example)

        chapter["examples"] = normalized

    # -------------------------------------------------

    @staticmethod
    def _normalize_quotes(chapter):

        quotes = chapter.get("quotes", [])

        normalized = []

        for quote in quotes:

            if isinstance(quote, str):

                normalized.append(
                    {
                        "text": quote,
                        "author": "Unknown"
                    }
                )

            else:

                normalized.append(quote)

        chapter["quotes"] = normalized

    # -------------------------------------------------

    @staticmethod
    def _normalize_code_examples(chapter):

        code_examples = chapter.get("code_examples", [])

        normalized = []

        for item in code_examples:

            if isinstance(item, str):

                normalized.append(
                    {
                        "title": "Code Example",
                        "language": "",
                        "code": item,
                        "explanation": ""
                    }
                )

            else:

                normalized.append(item)

        chapter["code_examples"] = normalized

    # -------------------------------------------------

    @staticmethod
    def _normalize_tables(chapter):

        tables = chapter.get("tables", [])

        normalized = []

        for table in tables:

            if isinstance(table, str):

                normalized.append(
                    {
                        "title": "Table",
                        "headers": [],
                        "rows": []
                    }
                )

            else:

                normalized.append(table)

        chapter["tables"] = normalized