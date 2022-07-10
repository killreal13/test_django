from django.urls import path, re_path
from .views import SignUp, shortener, user_links, return_url

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='signup'),
    path('', shortener, name='shortener'),
    re_path(r'^(\w{6})', return_url),
    re_path(r'^(\d)', user_links, name='mylinks')
]
