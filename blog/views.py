from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostLV(ListView):
    model = Post
    paginate_by = 4


class PostDV(DetailView):
    model = Post

