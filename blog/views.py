from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from blog.models import Posts
# Create your views here.


def blog_view(request, **kwargs):
    posts = Posts.objects.filter(status=1)
    context = {"posts": posts}
    return render(request, "blog/blog.html", context)


def blog_single(request, pid):
    posts = get_list_or_404(Posts, pk=pid, status=1)
    context = {"posts": posts}
    return render(request, "blog/single.html", context)

