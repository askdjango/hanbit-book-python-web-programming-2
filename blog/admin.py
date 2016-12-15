from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_length', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['title'],
    }

    def content_length(self, post):
        return '{}글자'.format(len(post.content))


admin.site.register(Post, PostAdmin)

