from django.urls import path

from . import views

urlpatterns = [

    path("login/",views.login_view,name="login",),
    path("signup/",views.signup_view,name="signup",),
    path("create-session/",views.create_session,name="create_session",),
    path("oauth/",views.oauth_callback,name="oauth_callback",),
    path("logout/",views.logout_view,name="logout",),
    path("forgot-password/",views.forgot_password_view,name="forgot_password",),
    path("reset-password/",views.reset_password_view,name="reset_password",),
]