from django.conf.urls import url
from blog import views
from blog import views_fbv

urlpatterns = [
    # url(r'^$', views.PostLV.as_view(), name='index'),  # "blog:index"
    # url(r'^post/$', views.PostLV.as_view(), name='post_list'),
    # url(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    url(r'^$', views_fbv.post_list, name='index'),  # "blog:index"
    url(r'^post/$', views_fbv.post_list, name='post_list'),
    url(r'^post/(?P<slug>[-\w]+)/$', views_fbv.post_detail, name='post_detail'),
]

