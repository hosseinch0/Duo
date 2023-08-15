from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from blog.models import Post, Category
from users.models import Profile
# Create your views here.


def blog_view(request, **kwargs):
    if request.user.is_authenticated:
        if request.method == "GET":
            categories = Category.objects.all()
            posts = Post.objects.filter(status=1)
            profile = Profile.objects.filter()
            context = {"posts": posts, "profile": profile,
                       "categories": categories}
            return render(request, "blog/blog.html", context)


def blog_single(request, pid):
    posts = get_list_or_404(Post, pk=pid, status=1)
    context = {"posts": posts}
    return render(request, "blog/single.html", context)
