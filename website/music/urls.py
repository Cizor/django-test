from django.conf.urls import include,url
from . import views

app_name = 'music'

urlpatterns = [
	#/music/
    url(r'^$', views.index, name='index'),
	#/music/[number]
	url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),

	#/music/[number]/favorite/
	url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
]
