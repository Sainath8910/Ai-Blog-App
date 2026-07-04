from blogs.repositories.blog_repository import BlogRepository


class BlogUpdateService:

    def update_blog(

        self,

        blog,

        cleaned_data,

    ):

        blog.title = cleaned_data["title"]

        blog.description = cleaned_data["description"]

        blog.category = cleaned_data["category"]

        blog.language = cleaned_data["language"]

        blog.tone = cleaned_data["tone"]

        blog.target_audience = cleaned_data["target_audience"]

        blog.status = cleaned_data["status"]

        BlogRepository.save(blog)

        return blog