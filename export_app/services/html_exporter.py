from django.template.loader import render_to_string


class HTMLExporter:

    def __init__(self, blog):

        self.blog = blog

    def export(self):

        context = {

            "blog": self.blog,

            "chapters": self.blog.chapters.all(),

        }

        return render_to_string(

            "export/html_export.html",

            context,

        )