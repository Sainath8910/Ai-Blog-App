from django.urls import path
from . import views

app_name = "export"

urlpatterns = [

    path(
        "markdown/<int:blog_id>/",
        views.export_markdown,
        name="markdown",
    ),
    path(
    "html/<int:blog_id>/",
    views.export_html,
    name="html",
),
path(
    "docx/<int:blog_id>/",
    views.export_docx,
    name="docx",
),

]