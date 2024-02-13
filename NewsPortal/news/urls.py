from django.urls import path
from .views import *


urlpatterns = [
    path('', NewsList.as_view(), name='news.html'),
    path('<int:id>/', NewsDetail.as_view()),
    path('search/', NewsSearch.as_view(), name='news_search.html'),
]