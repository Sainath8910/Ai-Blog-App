from django.urls import path

from .views import (
    GenerateBlogView,
    DashboardView,
    blog_detail,
    my_blogs,
    edit_blog,
    delete_blog,
    update_blog,
    regenerate_paragraph,
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
    path(
    "<int:blog_id>/delete/",
    delete_blog,
    name="delete",
),
path(

    "<int:blog_id>/update/",

    update_blog,

    name="update",

),
path(
    "regenerate/paragraph/",
    regenerate_paragraph,
    name="regenerate_paragraph",
),
]