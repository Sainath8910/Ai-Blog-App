"""
Pydantic models for the AI Blog Engine.
"""

from typing import List

from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Blog Information
# ---------------------------------------------------------

class BlogInfo(BaseModel):
    topic: str
    language: str
    tone: str
    blog_type: str
    target_audience: str


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

class Metadata(BaseModel):
    title: str
    slug: str
    description: str
    keywords: List[str] = Field(default_factory=list)
    category: str
    tags: List[str] = Field(default_factory=list)


# ---------------------------------------------------------
# Image
# ---------------------------------------------------------

class Image(BaseModel):
    prompt: str
    path: str = ""
    alt_text: str


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

class Example(BaseModel):
    title: str
    description: str


# ---------------------------------------------------------
# Quote
# ---------------------------------------------------------

class Quote(BaseModel):
    text: str
    author: str


class KeyTakeaway(BaseModel):
    title: str
    description: str
# ---------------------------------------------------------
# Code Example
# ---------------------------------------------------------

class CodeExample(BaseModel):
    title: str
    language: str
    code: str
    explanation: str


# ---------------------------------------------------------
# Table
# ---------------------------------------------------------

class Table(BaseModel):
    title: str
    headers: List[str]
    rows: List[List[str]]


# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------

class Hero(BaseModel):
    title: str
    subtitle: str
    summary: str
    image: Image

class Step(BaseModel):
    title: str
    description: str
# ---------------------------------------------------------
# Chapter
# ---------------------------------------------------------

class Chapter(BaseModel):
    id: int
    purpose: str
    title: str

    paragraphs: List[str] = Field(default_factory=list)

    bullet_points: List[str] = Field(default_factory=list)

    numbered_steps: List[Step] = Field(default_factory=list)

    tips: List[str] = Field(default_factory=list)

    warnings: List[str] = Field(default_factory=list)

    notes: List[str] = Field(default_factory=list)

    examples: List[Example] = Field(default_factory=list)

    quotes: List[Quote] = Field(default_factory=list)

    code_examples: List[CodeExample] = Field(default_factory=list)

    tables: List[Table] = Field(default_factory=list)

    image: Image


# ---------------------------------------------------------
# FAQ
# ---------------------------------------------------------

class FAQ(BaseModel):
    question: str
    answer: str


# ---------------------------------------------------------
# Resources
# ---------------------------------------------------------

class Resources(BaseModel):
    official_docs: List[str] = Field(default_factory=list)
    recommended_tools: List[str] = Field(default_factory=list)
    further_reading: List[str] = Field(default_factory=list)


# ---------------------------------------------------------
# CTA
# ---------------------------------------------------------

class CallToAction(BaseModel):
    type: str
    title: str
    description: str
    button_text: str
    button_link: str = ""


# ---------------------------------------------------------
# Conclusion
# ---------------------------------------------------------

class Conclusion(BaseModel):
    paragraphs: List[str] = Field(default_factory=list)
    image: Image


# ---------------------------------------------------------
# Main Blog Model
# ---------------------------------------------------------

class Blog(BaseModel):
    blog_info: BlogInfo

    metadata: Metadata

    hero: Hero

    chapters: List[Chapter]

    key_takeaways: List[KeyTakeaway] = Field(default_factory=list)

    resources: Resources | None = None

    call_to_action: CallToAction | None = None


    faq: List[FAQ] = Field(default_factory=list)

    conclusion: Conclusion
