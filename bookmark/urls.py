from django.conf.urls import url
from bookmark import views

urlpatterns = [
    url(r'^$', views.bookmark_list, name='bookmark_list'),
    url(r'^(?P<pk>\d+)/$', views.bookmark_detail, name='bookmark_detail'),
]

