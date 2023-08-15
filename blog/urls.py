from django.urls import path, include
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path("", blog_view, name="home"),
    path('<int:pid>', blog_single, name="single"),
    path("api/v1/", include("blog.api.v1.urls")),
]
