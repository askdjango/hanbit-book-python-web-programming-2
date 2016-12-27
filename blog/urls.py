from django.conf.urls import url
from blog.views import PostLV

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),  # "blog:index"
    url(r'^post/$', PostLV.as_view(), name='post_list'),
]

