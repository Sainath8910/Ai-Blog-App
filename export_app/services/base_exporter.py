from blogs.models import Blog


class BaseExporter:

    def __init__(self, blog: Blog):
        self.blog = blog
        self.chapters = blog.chapters.all()