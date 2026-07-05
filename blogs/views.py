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
from core.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
import json
@method_decorator(login_required, name="dispatch")
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

@method_decorator(login_required, name="dispatch")
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
    


@login_required
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

@login_required
def my_blogs(request):

    search = request.GET.get("q", "").strip()

    category = request.GET.get("category", "").strip()

    status = request.GET.get("status", "").strip()

    blogs = BlogRepository.get_user_blogs(

        request.user["id"],

        search,

        category,

        status,

    )

    paginator = Paginator(

        blogs,

        6,

    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    categories = Blog.objects.filter(

        user_id=request.user["id"],

        is_deleted=False,

    ).values_list(

        "category",

        flat=True,

    ).distinct()

    return render(

        request,

        "blogs/my_blogs.html",

        {

            "page_obj": page_obj,

            "search": search,

            "selected_category": category,

            "selected_status": status,

            "categories": categories,

        },

    )
@login_required
def edit_blog(request, blog_id):

    blog = BlogRepository.get_blog(blog_id)

    if str(blog.user_id) != request.user["id"]:
        return redirect("blogs:my_blogs")

    return render(
        request,
        "blogs/edit_blog.html",
        {
            "blog": blog,
            "chapters": blog.chapters.all(),
        },
    )
@login_required
@require_POST
def delete_blog(request, blog_id):

    try:

        blog = BlogRepository.get_blog(blog_id)

        if str(blog.user_id) != request.user["id"]:

            return JsonResponse(
                {
                    "success": False,
                    "message": "Permission denied."
                },
                status=403,
            )

        BlogRepository.delete_blog(blog)

        return JsonResponse(
            {
                "success": True,
            }
        )

    except Blog.DoesNotExist:

        return JsonResponse(
            {
                "success": False,
                "message": "Blog not found."
            },
            status=404,
        )
@login_required
@require_POST
def update_blog(request, blog_id):

    blog = BlogRepository.get_blog(blog_id)

    if str(blog.user_id) != request.user["id"]:

        return JsonResponse(

            {

                "success":False,

                "message":"Permission denied"

            },

            status=403,

        )

    data = json.loads(request.body)

    BlogRepository.update_blog(

        blog,

        data,

    )

    return JsonResponse(

        {

            "success":True

        }

    )