from functools import wraps
from django.shortcuts import redirect
from django.http import JsonResponse


def login_required(view_func):

    @wraps(view_func)

    def wrapper(request, *args, **kwargs):

        if "user" not in request.session:

            return redirect("login")

        request.user = request.session["user"]

        return view_func(request, *args, **kwargs)

    return wrapper


def anonymous_required(view_func):

    @wraps(view_func)

    def wrapper(request, *args, **kwargs):

        if "user" in request.session:

            return redirect("blogs:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper