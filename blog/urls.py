from django.urls import path, include
from blog.views import PostListView, PostDetailView, PostDeleteView, PostUpdateView, PostCreateView


app_name = 'blog'

urlpatterns = [
    # path("", blog_view, name="home"),
    # path('<int:pid>', blog_single, name="single"),
    path("post/", PostListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="single"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("post/create/", PostCreateView.as_view(), name="create"),
    path("api/v1/", include("blog.api.v1.urls")),
]
