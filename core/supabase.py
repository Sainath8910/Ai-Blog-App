import os

from supabase import Client, create_client


SUPABASE_URL = os.getenv("SUPABASE_URL")

SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

SUPABASE_SERVICE_ROLE_KEY = os.getenv(
    "SUPABASE_SERVICE_ROLE_KEY"
)


# Client used for authentication
auth_client: Client = create_client(
    SUPABASE_URL,
    SUPABASE_ANON_KEY
)


# Client used for privileged backend operations
admin_client: Client = create_client(
    SUPABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY
)