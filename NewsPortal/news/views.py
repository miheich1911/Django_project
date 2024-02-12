from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import *


class NewsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()
    #     context['next_sale'] = None

    def get_queryset(self):
        queryset = Post.objects.filter(post_type='NW')
        return queryset


class NewsDetail(DetailView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/news_id.html'
    context_object_name = 'news_id'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = Post.objects.filter(post_type='NW')
        return queryset


