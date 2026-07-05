from ai_pipeline.providers.llm.llm_manager import LLMManager
from ai_pipeline.providers.llm.llm_manager import LLMManager
from ai_pipeline.pipeline.image_generator import ImageGenerator
from .storage_service import StorageService


IMAGE_PROMPT_SYSTEM = """
You are an expert prompt engineer.

Generate a highly detailed prompt for an AI image generator.

Rules:
- Photorealistic
- Cinematic lighting
- High quality
- No text
- No watermark
- Return ONLY the image prompt.
"""
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
CHAPTER_SYSTEM_PROMPT = """
You are an expert blog editor.

Improve the given chapter.

Rules:
- Improve readability.
- Improve grammar.
- Improve flow.
- Preserve meaning.
- Keep approximately same length.

Return ONLY valid JSON.

{
    "title":"...",
    "paragraphs":["..."],
    "bullet_points":["..."]
}
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
    
    @staticmethod
    def regenerate_image(
        paragraphs,
        user_id,
        generation_uuid,
        image_name,
    ):

        llm = LLMManager()

        prompt = llm.generate(
            system_prompt=IMAGE_PROMPT_SYSTEM,
            user_prompt="\n\n".join(paragraphs),
        ).strip()

        generated = ImageGenerator().generate(
            prompt=prompt
        )

        stored = StorageService().upload_image(
            image=generated,
            user_id=user_id,
            generation_uuid=generation_uuid,
            image_name=image_name,
        )

        return stored
    @staticmethod
    def generate_image_prompt(
        paragraphs,
    ):

        llm = LLMManager()

        return llm.generate(

            system_prompt=IMAGE_PROMPT_SYSTEM,

            user_prompt="\n\n".join(paragraphs),

        ).strip()
    @staticmethod
    def regenerate_chapter(
        title,
        paragraphs,
        bullet_points,
        tone,
        audience,
    ):

        import json

        llm = LLMManager()

        prompt = f"""
    Title:
    {title}

    Tone:
    {tone}

    Audience:
    {audience}

    Paragraphs:
    {json.dumps(paragraphs)}

    Bullet Points:
    {json.dumps(bullet_points)}
    """

        response = llm.generate(
            system_prompt=CHAPTER_SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        return json.loads(response)