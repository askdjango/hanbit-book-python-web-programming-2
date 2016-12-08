from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
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


'''
class BookmarkDV(DetailView):
    model = Bookmark

bookmark_detail = BookmarkDV.as_view()
'''

def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    return render(request, 'bookmark/bookmark_detail.html', {
        'bookmark': bookmark,
    })

