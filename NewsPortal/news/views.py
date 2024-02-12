from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import *


class NewsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/news_id.html'
    context_object_name = 'news_id'
    pk_url_kwarg = 'id'




