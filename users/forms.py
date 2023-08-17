from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms


class RegistrationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=35)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
