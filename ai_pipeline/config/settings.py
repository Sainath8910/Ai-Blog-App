"""
Global configuration for the AI Pipeline.

This module should NEVER call load_dotenv().
Django loads the project .env during startup.

All modules in the pipeline should import configuration
only from this file.
"""

from pathlib import Path
import os

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# API Keys
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
# ==========================================================
# Supabase
# ==========================================================

SUPABASE_URL = os.getenv("SUPABASE_URL")

SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

SUPABASE_STORAGE_BUCKET = os.getenv(
    "SUPABASE_STORAGE_BUCKET",
    "blog-images"
)

# ==========================================================
# LLM Configuration
# ==========================================================

PRIMARY_LLM = os.getenv(
    "PRIMARY_LLM",
    "gemini"
)

BACKUP_LLMS = [
    "openrouter_deepseek",
    "openrouter_qwen",
    "gemini_flash_lite",
    "gemini_20_flash",
    "openrouter",
    "openrouter_llama33",
]

CONTENT_MODEL = os.getenv(
    "CONTENT_MODEL",
    "gemini-2.5-flash"
)

TEMPERATURE = float(
    os.getenv("TEMPERATURE", "0.7")
)

TOP_P = float(
    os.getenv("TOP_P", "0.95")
)

MAX_OUTPUT_TOKENS = int(
    os.getenv("MAX_OUTPUT_TOKENS", "8192")
)

# ==========================================================
# Image Generation
# ==========================================================

IMAGE_PRIMARY_PROVIDER = "pollinations_flux_dev"

IMAGE_BACKUP_PROVIDERS = [
    
    "pollinations",
    "pollinations_turbo",
    "cloudflare_sdxl",
    "cloudflare_dreamshaper",
]

IMAGE_MODEL = os.getenv(
    "IMAGE_MODEL",
    "black-forest-labs/FLUX.1-schnell"
)

IMAGE_WIDTH = 1024

IMAGE_HEIGHT = 1024

IMAGE_TIMEOUT = 180

IMAGE_EXTENSION = ".png"

# ==========================================================
# Search
# ==========================================================

SEARCH_PROVIDER = os.getenv(
    "SEARCH_PROVIDER",
    "tavily"
)

# ==========================================================
# Blog Defaults
# ==========================================================

DEFAULT_LANGUAGE = os.getenv(
    "DEFAULT_LANGUAGE",
    "English"
)

DEFAULT_TONE = os.getenv(
    "DEFAULT_TONE",
    "Professional"
)

DEFAULT_BLOG_TYPE = os.getenv(
    "DEFAULT_BLOG_TYPE",
    "Technical"
)

DEFAULT_TARGET_AUDIENCE = os.getenv(
    "DEFAULT_TARGET_AUDIENCE",
    "Beginners"
)

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

# ==========================================================
# OpenRouter
# ==========================================================

OPENROUTER_BASE_URL = (
    "https://openrouter.ai/api/v1/chat/completions"
)

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openrouter/free"
)

# ==========================================================
# Validation
# ==========================================================

REQUIRED_API_KEYS = {
    "GEMINI_API_KEY": GEMINI_API_KEY,
    "HUGGINGFACE_API_KEY": HUGGINGFACE_API_KEY,
    "TAVILY_API_KEY": TAVILY_API_KEY,
}