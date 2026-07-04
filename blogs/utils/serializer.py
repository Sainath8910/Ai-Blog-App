from pydantic import BaseModel


def serialize(value):
    """
    Convert Pydantic models into plain Python
    objects suitable for Django JSONField.
    """

    if value is None:
        return None

    if isinstance(value, BaseModel):
        return value.model_dump()

    if isinstance(value, list):
        return [
            serialize(item)
            for item in value
        ]

    if isinstance(value, dict):
        return {
            key: serialize(val)
            for key, val in value.items()
        }

    return value