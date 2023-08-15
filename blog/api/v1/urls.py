from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("post/", PostListView.as_view(), name="api-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="api-detail"),
]
