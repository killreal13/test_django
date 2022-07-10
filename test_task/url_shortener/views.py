from django import forms
from django.urls import reverse_lazy
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Link


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'


class ShortenerUserForm(ModelForm):
    class Meta:
        model = Link
        fields = ['long_url']


class ShortenerForm(forms.Form):
    long_url = forms.URLField()


def return_url(request, url):
    redirect_queryset = Link.objects.values().get(short_url=request.build_absolute_uri())
    return redirect(redirect_queryset['long_url'], permanent=True)


def shortener(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ShortenerUserForm(request.POST)
            if form.is_valid():
                try:
                    link = Link.objects.get(user=request.user,
                                            long_url=form.cleaned_data.get('long_url'))
                except Exception:
                    form.instance.user = User.objects.get(username=request.user)
                    form.save()
                    link = Link.objects.all().filter(user=request.user)[::-1][0]
            else:
                link = ''
        else:
            form = ShortenerForm(request.POST)
            if form.is_valid():
                try:
                    link = Link.objects.get(long_url=form.cleaned_data.get('long_url'))
                except Exception:
                    try:
                        user = User.objects.get(username='Anonymous', password='Anonymous')
                    except Exception:
                        user = User(username='Anonymous', password='Anonymous')
                        user.save()
                        user = User.objects.get(username='Anonymous', password='Anonymous')
                    new_url = Link(user=user, long_url=form.cleaned_data.get('long_url'))
                    new_url.save()
                    link = Link.objects.all().filter(user=user)[::-1][0]
            else:
                link = ''
    else:
        if request.user.is_authenticated:
            form = ShortenerUserForm()
            link = ''
        else:
            form = ShortenerForm()
            link = ''
    return render(request, 'shortener.html', {'form': form, 'link': link})


def user_links(request, id):
    context = {}
    try:
        context['links'] = Link.objects.all().filter(user=id)
    except Exception:
        context['links'] = ''
    return render(request, 'my_links.html', context)

