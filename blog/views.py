from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog


class BlogList(ListView):
    model = Blog

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
