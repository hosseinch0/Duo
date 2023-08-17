from django.urls import path
from users.views import *


app_name = "users"


urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", ProfileView.as_view(), name="profile")
]
