from django.conf import settings
from django.shortcuts import render

from core.decorators import login_required


@login_required
def dashboard_view(request):

    context = {

        "email": request.email,
        "user_id": request.user_id,

        "blogs_created": 0,
        "draft_blogs": 0,
        "published_blogs": 0,
        "images_generated": 0,

        "SUPABASE_URL": settings.SUPABASE_URL,
        "SUPABASE_ANON_KEY": settings.SUPABASE_ANON_KEY,

    }
    return render(
        request,
        "blogs/dashboard.html",
        context
    )