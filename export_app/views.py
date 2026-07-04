from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .services.html_exporter import HTMLExporter
from blogs.models import Blog
from .services.markdown_exporter import MarkdownExporter
from io import BytesIO
from .services.docx_exporter import DocxExporter

def export_markdown(request, blog_id):

    blog = get_object_or_404(
        Blog.objects.prefetch_related("chapters"),
        pk=blog_id,
        is_deleted=False,
    )

    markdown = MarkdownExporter(blog).export()

    filename = f"{blog.slug}.md"

    response = HttpResponse(
        markdown,
        content_type="text/markdown",
    )

    response["Content-Disposition"] = (
        f'attachment; filename="{filename}"'
    )

    return response


def export_html(request, blog_id):

    blog = get_object_or_404(

        Blog.objects.prefetch_related("chapters"),

        pk=blog_id,

        is_deleted=False,

    )

    html = HTMLExporter(blog).export()

    response = HttpResponse(

        html,

        content_type="text/html",

    )

    response["Content-Disposition"] = (

        f'attachment; filename="{blog.slug}.html"'

    )

    return response





def export_docx(request, blog_id):

    blog = get_object_or_404(

        Blog.objects.prefetch_related("chapters"),

        pk=blog_id,

        is_deleted=False,

    )

    exporter = DocxExporter(blog)

    document = exporter.export()

    buffer = BytesIO()

    document.save(buffer)

    buffer.seek(0)

    response = HttpResponse(

        buffer.read(),

        content_type=(
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ),

    )

    response["Content-Disposition"] = (

        f'attachment; filename="{blog.slug}.docx"'

    )

    return response


