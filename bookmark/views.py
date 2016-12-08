from django.shortcuts import render
from django.views.generic import ListView
from .models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark

bookmark_list = BookmarkLV.as_view()
