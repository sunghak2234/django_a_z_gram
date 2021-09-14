from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
