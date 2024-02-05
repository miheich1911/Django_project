from django.views.generic import ListView
from .models import *


class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
