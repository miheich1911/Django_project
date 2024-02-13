from django_filters import FilterSet
from .models import *


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'date_in': ['gt'],
             }