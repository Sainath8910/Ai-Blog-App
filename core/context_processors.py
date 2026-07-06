from django.conf import settings


def app_context(request):
    """
    Global variables available in all templates.
    """

    return {

        # ----------------------------------------
        # Application
        # ----------------------------------------

        "APP_NAME": "AI Blog Generator",

        "APP_VERSION": "v1.0",

        # ----------------------------------------
        # Current User
        # ----------------------------------------

        "CURRENT_USER": request.session.get("user"),

        # ----------------------------------------
        # Supabase
        # ----------------------------------------

        "SUPABASE_URL": settings.SUPABASE_URL,

        "SUPABASE_ANON_KEY": settings.SUPABASE_ANON_KEY,

    }

def app_settings(request):
    return {
        "APP_URL": settings.APP_URL,
    }