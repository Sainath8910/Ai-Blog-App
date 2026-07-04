from dataclasses import dataclass


@dataclass(slots=True)
class StoredImage:

    storage_path: str

    public_url: str

    prompt: str

    alt_text: str

    provider: str