
from django.db import models
from martor.models import MartorField


class Blog(models.Model):
    slug = models.CharField(max_length=24, primary_key=True)
    draft = models.BooleanField(default=True)
    body = MartorField()
