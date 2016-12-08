from django.contrib import admin
from .models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['title', 'linked_url']

    def linked_url(self, bookmark):
        return '<a href="{url}" target="_blank">{url}</a>'.format(url=bookmark.url)
    linked_url.allow_tags = True


# admin.site.register(Bookmark, BookmarkAdmin)

