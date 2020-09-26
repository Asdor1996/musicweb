from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musics$', views.MusicListView.as_view(), name='musics'),
    url(r'^music/(?P<pk>\d+)$', views.MusicDetailView.as_view(), name='music-detail'),
   # url(r'music/(?P<pk>[-\w]+)/renew/$',  views.renew_music_librarian, name='renew-music-librarian')
]

