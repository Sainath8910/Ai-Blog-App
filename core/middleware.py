from .auth import authenticate_request


class SupabaseAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = authenticate_request(request)

        request.supabase_user = user

        if user:

            request.user_id = user.id
            request.email = user.email

            request.role = (
                user.user_metadata.get("role", "authenticated")
                if user.user_metadata
                else "authenticated"
            )

        else:

            request.user_id = None
            request.email = None
            request.role = None

        return self.get_response(request)