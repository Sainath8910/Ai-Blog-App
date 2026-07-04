from functools import wraps
from django.shortcuts import redirect
from django.http import JsonResponse


def supabase_login_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user_id is None:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Authentication required."
                },
                status=401,
            )

        return view_func(request, *args, **kwargs)

    return wrapper




def anonymous_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user_id:
            return redirect("/dashboard/")

        return view_func(request, *args, **kwargs)

    return wrapper