from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('albums', views.albums, name='albums'),
	path('album/add', views.add_album, name='album-add'),
	path('album/<int:pk>', views.album, name='album-detail'),
	path('album/<int:pk>/del', views.del_album, name='album-del'),	

	path('genres', views.genres, name='genres'),
	path('genre/<int:pk>', views.genre, name='genre-detail'),

	path('bands', views.bands, name='bands'),
	path('band/<int:pk>', views.band, name='band-detail'),

	path('videos', views.videos, name='videos'),
	path('video/<int:pk>', views.video, name='video-detail'),

	path('concerts', views.concerts, name='concerts'),
	path('concert/<int:pk>', views.concert, name='concert-detail'),

	path('track/<int:pk>', views.track, name='track-detail'),	
	path('track/<int:pk>/del', views.del_track, name='track-del'),


    path('users', views.users, name='users'),
	path('user/<int:pk>', views.user, name='user-detail'),	
	path('user/<int:pk>/change', views.change_group, name='user-change'),
    path('profile', views.profile, name='profile'),
]