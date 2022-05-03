from django.db import models
from django.utils.text import slugify
from martor.models import MartorField


class Blog(models.Model):
    draft = models.BooleanField(default=True)
    title = models.CharField(max_length=24)
    slug = models.CharField(max_length=24, primary_key=True, blank=True)
    body = MartorField()

    def save(self, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        return super().save(kwargs)
