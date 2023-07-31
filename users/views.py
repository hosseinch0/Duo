from django.shortcuts import render,redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from users.forms import RegistrationForm

# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user != None:
                print("User found")
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Authentication successful, Logged in successfully")
                return redirect("/")
            else:
                messages.add_message(request, messages.ERROR, "Authentication failed")
    
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
                messages.add_message(request, messages.SUCCESS, "Signed Up successfully !")
            else:
                print("invalid form")
                messages.add_message(request, messages.ERROR, "Account did not registered !!!")
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "Users/signup.html", context)
    else:
        return redirect('/')



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, "Successfully logged out")
    else:
        messages.add_message(request, messages.ERROR, "Logging out failed")
    return redirect("/")