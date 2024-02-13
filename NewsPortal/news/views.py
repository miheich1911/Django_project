from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import *
from .filters import NewsFilter


class NewsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 1


class NewsDetail(DetailView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/news_id.html'
    context_object_name = 'news_id'
    pk_url_kwarg = 'id'


class NewsSearch(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/news_search.html'
    context_object_name = 'news'
    paginate_by = 1

    def qet_queryset(self):
        queryset = super().get_queryset()
        filterset = NewsFilter(self.request.GET, queryset=queryset)
        return filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



