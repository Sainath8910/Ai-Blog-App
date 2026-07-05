from .auth import authenticate_request


from .auth import verify_token


class SupabaseAuthMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        session_user = request.session.get("user")

        if session_user:

            request.user_id = session_user["id"]
            request.email = session_user["email"]
            request.role = "authenticated"

        else:

            request.user_id = None
            request.email = None
            request.role = None

        return self.get_response(request)