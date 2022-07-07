from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = ...
    template_name = ...

