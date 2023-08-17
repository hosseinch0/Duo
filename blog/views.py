from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.forms.models import BaseModelForm
from blog.models import Post, Category
from users.models import Profile
from blog.forms import PostForm
# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    """ A COMPLETE LIST OF THE POSTS PAGINATED TROUGH PAGES """
    paginate_by = 9
    queryset = Post.objects.filter(status=1)
    ordering = "-created_at"
    template_name = "blog/blog.html"

    """ if user is not logged in will be redirected to the login page """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/users/login/')
        return super().dispatch(request, *args, **kwargs)

    """ sending the context data to the template """

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["categories"] = Category.objects.all()
        context_data["posts"] = Post.objects.filter(status=1)
        context_data["profile"] = Profile.objects.filter(
            user=self.request.user)
        return context_data


class PostDetailView(LoginRequiredMixin, DetailView, PermissionRequiredMixin):
    """ single posts view """
    model = Post
    template_name = "blog/single.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    """ Custom Post Creation via custom templates """
    model = Post
    fields = ["title", "content",
              "category", "published_at", "image"]
    template_name = "blog/post_create.html"
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DetailView, PermissionRequiredMixin):
    """ DELETING THE POST """
    model = Post
    context_object_name = "post"
    template_name = "blog/post_delete.html"
    success_url = "/blog/post/"


class PostUpdateView(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    """ UPDATING THE POSTS PUT OR PATCH """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = "/blog/post/"
