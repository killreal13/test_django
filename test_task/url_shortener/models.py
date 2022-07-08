from django.db import models
from django.contrib.auth.models import User
from .utils import shortener


class Link(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    long_url = models.CharField(max_length=25)
    short_url = models.CharField(max_length=25, unique=False, blank=True)

    def save(self, *args, **kwargs):
        self.short_url = shortener(r'http://127.0.0.1:8000/', self.long_url)
        super(Link, self).save(*args, **kwargs)
    

