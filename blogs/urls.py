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
    regenerate_image,
    regenerate_chapter,
    regenerate_entire_blog,
)

app_name = "blogs"

urlpatterns = [

    path("", DashboardView.as_view(), name="dashboard"),

    path("generate/", GenerateBlogView.as_view(), name="generate"),

    path("my/", my_blogs, name="my_blogs"),

    path("regenerate/paragraph/", regenerate_paragraph, name="regenerate_paragraph"),

    path("regenerate/image/", regenerate_image, name="regenerate_image"),

    path("regenerate/chapter/", regenerate_chapter, name="regenerate_chapter"),

    path("regenerate/blog/", regenerate_entire_blog, name="regenerate_blog"),

    path("<int:blog_id>/edit/", edit_blog, name="edit"),

    path("<int:blog_id>/update/", update_blog, name="update"),

    path("<int:blog_id>/delete/", delete_blog, name="delete"),

    path("<int:blog_id>/", blog_detail, name="detail"),
]