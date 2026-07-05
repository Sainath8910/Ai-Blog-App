from django.shortcuts import render
from django.http import JsonResponse
from core.decorators import anonymous_required
import json
from django.views.decorators.http import require_POST
from core.auth import verify_token
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from core.decorators import anonymous_required

@anonymous_required
def login_view(request):

    return render(

        request,

        "authentication/login.html",

    )

@anonymous_required
def signup_view(request):

    return render(

        request,

        "authentication/signup.html",

    )



def session_view(request):
    return JsonResponse(
        {
            "authenticated": request.user_id is not None,
            "user_id": request.user_id,
            "email": request.email,
            "role": request.role,
        }
    )

@csrf_exempt
@require_POST
def create_session(request):

    try:

        body = json.loads(request.body)

        access_token = body.get("access_token")

        if not access_token:

            return JsonResponse(

                {

                    "success": False,

                    "message": "Access token missing."

                },

                status=400

            )

        user = verify_token(access_token)

        if user is None:

            return JsonResponse(

                {

                    "success": False,

                    "message": "Invalid access token."

                },

                status=401

            )

        request.session["user"] = {

            "id": str(user.id),

            "email": user.email,

        }

        request.session["access_token"] = access_token

        request.session.save()
        """print("=" * 50)
        print("create_session called")
        print("Access Token:", access_token[:20], "...")
        print("User:", user)"""
        return JsonResponse(

            {

                "success": True,

                "user": {

                    "id": str(user.id),

                    "email": user.email,

                }

            }

        )

    except Exception as e:

        return JsonResponse(

            {

                "success": False,

                "message": str(e),

            },

            status=500

        )


@require_POST
def logout_view(request):

    request.session.flush()

    response = JsonResponse({

        "success": True,

    })

    return response

def oauth_callback(request):

    return render(

        request,

        "authentication/oauth_callback.html",

    )

def forgot_password_view(request):

    return render(

        request,

        "authentication/forgot_password.html",

    )


def reset_password_view(request):

    return render(

        request,

        "authentication/reset_password.html",

    )