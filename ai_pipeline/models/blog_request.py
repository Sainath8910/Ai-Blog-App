from pydantic import BaseModel


class BlogRequest(BaseModel):

    topic: str

    content_brief: str

    target_audience: str

    tone: str

    length: str

    keywords: list[str]