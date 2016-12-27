from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostLV(ListView):
    model = Post
    paginate_by = 4

