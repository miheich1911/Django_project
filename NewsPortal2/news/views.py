from django.views.generic import ListView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

