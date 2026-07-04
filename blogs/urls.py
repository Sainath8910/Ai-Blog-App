from django.urls import path

from .views import (
    GenerateBlogView,
    DashboardView,
    blog_detail,
    my_blogs,
    edit_blog,
)

app_name = "blogs"

urlpatterns = [

    path(
        "",
        DashboardView.as_view(),
        name="dashboard",
    ),

    path(
        "generate/",
        GenerateBlogView.as_view(),
        name="generate",
    ),
    path("<int:blog_id>/",blog_detail,name="detail",),
    path(
        "my/",
        my_blogs,
        name="my_blogs",
    ),
    path(
    "<int:blog_id>/edit/",
    edit_blog,
    name="edit",),
]