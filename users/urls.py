from users.views import *
from django.urls import path


app_name = "users"


urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile")
]