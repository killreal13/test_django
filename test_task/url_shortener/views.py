from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .models import Link
from django.forms import ModelForm
from .utils import shortener as sh
from django.contrib.auth.models import User
import json

@csrf_exempt
def main(request):
    return render(request, 'shortener.html')


class ShortenerForm(ModelForm):
    class Meta:
        model = Link
        fields = ['long_url']
        # template_name = 'shortener.html'
        # success_url = reverse_lazy('shortener')


def shortener(request):
    result = 'smth'
    instance = Link.objects.all()
    if request.method == 'POST':
        form = ShortenerForm()
        form.user = User.objects.get(username=request.user)
        form.save()
        result = 'Your short url will appear here..'
    else:
        form = ShortenerForm()
        result = Link.Objects.get(user=User.objects.get(username=request.user))[0]
    return render(request, 'shortener.html', {'form': form, 'smth': result})
    # def shortener(self, form):
    #     context = {}
    #     try:
    #         data = json.loads(request.body)
    #         sh_url = sh(r'http://127.0.0.1:8000/', data['link'])
    #         user = User.objects.get(username=request.user)
    #         short_link = Link(user=user, long_url=data['link'], short_url=sh_url)
    #         short_link.save()
    #     except Exception:
    #         context['short_url'] = Link.objects.filter(user=request.user).order_by('short_url').reverse()[:1][0]
    #     return render(request, 'shortener.html', context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'

