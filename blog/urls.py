from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('single/<int:pid>', single_view, name="single"),
]