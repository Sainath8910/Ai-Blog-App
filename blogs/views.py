from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from blogs.repositories.blog_repository import BlogRepository
from ai_pipeline.models.blog_request import BlogRequest
from blogs.models import Blog
from .forms import BlogGenerationForm
from .services.blog_service import BlogService
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import BlogEditForm
from .services.blog_update_service import BlogUpdateService

class GenerateBlogView(TemplateView):
    template_name = "blogs/generate_blog.html"

    def get(self, request):

        if "user" not in request.session:
            return redirect("login")

        form = BlogGenerationForm()

        return self.render_to_response({
            "form": form,
        })

    def post(self, request):

        if "user" not in request.session:
            return redirect("login")

        form = BlogGenerationForm(request.POST)

        if not form.is_valid():

            return self.render_to_response({
                "form": form,
            })

        data = form.cleaned_data

        request_model = BlogRequest(

            topic=data["topic"],

            content_brief=data["content_brief"],

            target_audience=data["target_audience"],

            tone=data["tone"],

            length=data["length"],

            keywords=[
                keyword.strip()
                for keyword in data["keywords"].split(",")
                if keyword.strip()
            ],
        )

        try:

            service = BlogService()

            blog = service.generate(

                request=request_model,

                user_id=request.session["user"]["id"],

            )

            messages.success(
                request,
                "Blog generated successfully."
            )

            return redirect(
                "blogs:detail",
                blog.id,
            )

        except Exception as e:

            messages.error(
                request,
                str(e),
            )

            return self.render_to_response({
                "form": form,
            })
        
"""class PreviewBlogView(View):

    template_name = "blogs/preview_blog.html"

    def get(self, request, pk):

        blog = get_object_or_404(
            Blog.objects.prefetch_related("chapters"),
            pk=pk,
            is_deleted=False,
        )

        return render(
            request,
            self.template_name,
            {
                "blog": blog,
                "chapters": blog.chapters.all(),
            },
        )"""

class DashboardView(TemplateView):
    """
    User dashboard.
    """

    template_name = "blogs/dashboard.html"

    def get(self, request, *args, **kwargs):

        user = request.session.get("user")

        if not user:
            return redirect("login")

        user_id = user["id"]

        blogs = Blog.objects.filter(
            user_id=user_id,
            is_deleted=False,
        )

        total_blogs = blogs.count()

        draft_blogs = blogs.filter(
            status="draft"
        ).count()

        published_blogs = blogs.filter(
            status="published"
        ).count()

        recent_blogs = (
            blogs
            .order_by("-created_at")[:5]
        )

        total_images = 0

        for blog in recent_blogs:

            total_images += 2      # hero + conclusion

            total_images += (
                blog.chapters.count()
            )

        context = {

            "total_blogs": total_blogs,

            "draft_blogs": draft_blogs,

            "published_blogs": published_blogs,

            "recent_blogs": recent_blogs,

            "total_images": total_images,

            "storage_used": "Calculating...",

        }

        return self.render_to_response(context)
    



def blog_detail(request, blog_id):

    blog = BlogRepository.get_blog(blog_id)

    return render(

        request,

        "blogs/detail.html",

        {

            "blog": blog,

            "chapters": blog.chapters.all(),

        },

    )
def my_blogs(request):

    print("=" * 50)
    print("request.user_id:", request.user_id)

    blogs = BlogRepository.get_user_blogs(
        request.user_id
    )

    print("Blogs Count:", blogs.count())

    return render(
        request,
        "blogs/my_blogs.html",
        {
            "blogs": blogs,
        },
    )
def edit_blog(request, blog_id):

    blog = BlogRepository.get_blog(blog_id)

    if request.method == "POST":

        form = BlogEditForm(request.POST)

        if form.is_valid():

            BlogUpdateService().update_blog(
                blog,
                form.cleaned_data,
            )

            messages.success(
                request,
                "Blog updated successfully."
            )

            return redirect(
                "blogs:detail",
                blog.id,
            )

    else:

        form = BlogEditForm(
            initial={
                "title": blog.title,
                "description": blog.description,
                "category": blog.category,
                "language": blog.language,
                "tone": blog.tone,
                "target_audience": blog.target_audience,
                "status": blog.status,
            }
        )

    return render(
        request,
        "blogs/edit_blog.html",
        {
            "blog": blog,
            "chapters": blog.chapters.all(),
            "form": form,
        },
    )