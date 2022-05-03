from django.db import models


class Blog(models.Model):
    slug = models.CharField(max_length=24, primary_key=True)
