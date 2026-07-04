import uuid

from supabase import Client

from django.conf import settings

from core.supabase import admin_client

from ai_pipeline.models.generated_image import GeneratedImage

from blogs.dto.stored_image import StoredImage


class StorageService:

    def __init__(self):

        self.client: Client = admin_client

        self.bucket = settings.SUPABASE_STORAGE_BUCKET

    def upload_image(

        self,

        image: GeneratedImage,

        user_id: str,

        generation_uuid: str,

        image_name: str,

    ) -> StoredImage:

        filename = (
            f"{image_name}_"
            f"{uuid.uuid4().hex[:8]}"
            f"{image.extension}"
        )

        storage_path = (
            f"users/"
            f"{user_id}/"
            f"generations/"
            f"{generation_uuid}/"
            f"{filename}"
        )

        self.client.storage.from_(self.bucket).upload(

            path=storage_path,

            file=image.image_bytes,

            file_options={
                "content-type": image.mime_type,
                "upsert": False,
            },

        )

        public_url = (

            self.client
            .storage
            .from_(self.bucket)
            .get_public_url(storage_path)

        )

        return StoredImage(

            storage_path=storage_path,

            public_url=public_url,

            prompt=image.prompt,

            alt_text=image.alt_text,

            provider=image.provider,

        )
    def delete_image(

        self,

        storage_path: str,

    ) -> None:

        self.client.storage.from_(

            self.bucket

        ).remove([storage_path])

    def delete_generation_folder(

        self,

        files: list[str],

    ) -> None:
        self.client.storage.from_(

            self.bucket

        ).remove(files)