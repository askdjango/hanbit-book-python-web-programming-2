from django.shortcuts import render
from django.views.generic import ListView
from .models import Bookmark


'''
class BookmarkLV(ListView):
    model = Bookmark

bookmark_list = BookmarkLV.as_view()
'''

def bookmark_list(request):
    return render(request, 'bookmark/bookmark_list.html', {
        'bookmark_list': Bookmark.objects.all(),
    })

