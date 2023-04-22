from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'


class PostDetail(DetailView):
    model = Post
    template_name = 'news_pk.html'
    context_object_name = 'post'