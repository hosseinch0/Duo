from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView
from users.forms import RegistrationForm
from django.contrib import messages
from users.models import Profile
from typing import Any, Dict
from django import http
# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            print("post")
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user != None:
                print("User found")
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS, "Authentication successful, Logged in successfully")
                context = {"user": user}
                return render(request, "users/profile.html", context)
            else:
                messages.add_message(
                    request, messages.ERROR, "Authentication failed")

        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "Users/login.html", context)
    else:
        return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        if request.method == "POST":
            print("POST")
            form = RegistrationForm(request.POST)
            if form.is_valid():
                print("valid form")
                form.save()
                messages.add_message(
                    request, messages.SUCCESS, "Signed Up successfully !")
                return HttpResponseRedirect("/users/login/")
            else:
                print("invalid form")
                messages.add_message(
                    request, messages.ERROR, "Account did not registered !!!")
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "Users/signup.html", context)
    else:
        return redirect('/')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             "Successfully logged out")
    else:
        messages.add_message(request, messages.ERROR, "Logging out failed")
    return redirect("/")


class ProfileView(ListView, LoginRequiredMixin):

    model = Profile
    context_object_name = "profile"
    template_name = "Users/profile.html"

    def dispatch(self, request, *args, **kwargs):
        """ IF NOT AUTHENTICATED TO SEE THE PROFILE REDIRECTS TO THE LOGIN PAGE """
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/users/login")
        return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data["profile"] = Profile.objects.filter(
    #         user=self.request.user)
    #     return context_data
