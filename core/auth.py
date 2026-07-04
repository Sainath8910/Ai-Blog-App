from core.supabase import auth_client


def extract_token(request):
    """
    Extract access token from:
    1. Authorization header
    2. HttpOnly cookie
    """

    auth_header = request.headers.get("Authorization")

    if auth_header and auth_header.startswith("Bearer "):
        return auth_header.split(" ")[1]

    return request.COOKIES.get("access_token")


def verify_token(token):
    """
    Verify token using Supabase.
    """

    try:
        response = auth_client.auth.get_user(token)

        if response.user is None:
            return None

        return response.user

    except Exception:
        return None


def authenticate_request(request):

    token = extract_token(request)

    if not token:
        return None

    return verify_token(token)