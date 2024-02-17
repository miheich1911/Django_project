from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import NewsForm


class PostList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/post_id.html'
    context_object_name = 'post_id'
    pk_url_kwarg = 'id'


class PostSearch(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/post_search.html'
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'flatpages/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/create/':
            post.post_type = 'NW'
        else:
            post.post_type = 'AR'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    context_object_name = 'post'


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post.html')
    context_object_name = 'post'








