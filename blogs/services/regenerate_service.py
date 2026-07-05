from ai_pipeline.providers.llm.llm_manager import LLMManager


PARAGRAPH_SYSTEM_PROMPT = """
You are an expert blog editor.

Your task is to improve an existing paragraph.

Rules:
- Preserve the original meaning.
- Improve grammar.
- Improve readability.
- Make it slightly more engaging.
- Keep approximately the same length.
- Do not add markdown.
- Do not explain anything.
- Return ONLY the improved paragraph.
"""


class RegenerateService:

    @staticmethod
    def regenerate_paragraph(
        paragraph,
        chapter_title,
        tone,
        audience,
    ):

        llm = LLMManager()

        user_prompt = f"""
Chapter:
{chapter_title}

Tone:
{tone}

Audience:
{audience}

Current Paragraph:
{paragraph}
"""

        return llm.generate(
            system_prompt=PARAGRAPH_SYSTEM_PROMPT,
            user_prompt=user_prompt,
        ).strip()