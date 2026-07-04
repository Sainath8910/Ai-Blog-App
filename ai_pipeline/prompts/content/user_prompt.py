"""
Builds the user prompt for the Content Agent.
"""

from ai_pipeline.models.blog_request import BlogRequest


def build_user_prompt(
    request: BlogRequest,
) -> str:
    """
    Build the dynamic user prompt.

    Args:
        request:
            User blog generation request.

    Returns:
        A formatted prompt string.
    """

    keywords = ", ".join(request.keywords)

    prompt = f"""
Generate a high-quality blog using the following information.

====================================================

Blog Topic
----------
{request.topic}

Content Brief
-------------
{request.content_brief}

Target Audience
---------------
{request.target_audience}

Tone
----
{request.tone}

Blog Length
-----------
{request.length}

SEO Keywords
------------
{keywords}

====================================================

Generate the blog strictly according to the system instructions.

Return ONLY valid JSON.
"""

    return prompt.strip()