from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Album, Band, Concert, Genre, Track, Profile, Video, City
from django.contrib.auth.models import User, Group, Permission

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_album = Album.objects.all().count()
    num_band = Band.objects.all().count()
    num_concert = Concert.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_track = Track.objects.all().count()
    num_videos = Video.objects.all().count()
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context = {
            'num_album':num_album,
            'num_band':num_band,
            'num_concert':num_concert,
            'num_genre':num_genre,
            'num_track':num_track,
            'num_videos':num_videos,
    	},
    )

def albums(request):
    album_list = Album.objects.all()
    return render(
        request,
        'albums.html',
        context = {
            'album_list':album_list,
        },
    )

def genres(request):
    genre_list = Genre.objects.all()
    return render(
        request,
        'genres.html',
        context = {
            'genre_list':genre_list,
        },
    )

def bands(request):
    band_list = Band.objects.all()
    return render(
        request,
        'bands.html',
        context = {
            'band_list':band_list,
        },
    )

def videos(request):
    video_list = Video.objects.all()
    return render(
        request,
        'videos.html',
        context = {
            'video_list':video_list,
        },
    )
def concerts(request):
    concert_list = Concert.objects.all()
    return render(
        request,
        'concerts.html',
        context = {
            'concert_list':concert_list,
        },
    )

def album(request, pk):
    c_album = Album.objects.get(pk=pk)
    c_band = c_album.band
    c_tracks = Track.objects.filter(album__exact=c_album)
    return render(
        request,
        'album-detail.html',
        context = {
            'album':c_album,
            'band':c_band,
            'tracks':c_tracks,
        },
    )

def track(request, pk):
    c_track = Track.objects.get(pk=pk)
    c_album = c_track.album
    c_band = c_album.band
    return render(
        request,
        'track-detail.html',
        context = {
            'album':c_album,
            'band':c_band,
            'track':c_track,
        },
    )

def genre(request, pk):
    c_genre = Genre.objects.get(pk=pk)
    c_bands = Band.objects.filter(genre__exact=c_genre)
    return render(
        request,
        'genre-detail.html',
        context = {
            'genre':c_genre,
            'bands':c_bands,
        },
    )

def band(request, pk):
    c_band = Band.objects.get(pk=pk)
    c_albums = Album.objects.filter(band__exact=c_band)
    c_concerts = c_band.concerts
    return render(
        request,
        'band-detail.html',
        context = {
            'band':c_band,
            'albums':c_albums,
            'concerts': c_concerts,
        },
    )

def video(request, pk):
    c_video = Video.objects.get(pk=pk)
    c_track = Track.objects.filter(video__exact=c_video)
    c_album = c_track.album
    c_band = c_album.band
    return render(
        request,
        'video-detail.html',
        context = {
            'video':c_genre,
            'bands':c_bands,
        },
    )


def concert(request, pk):
    c_concert = Concert.objects.get(pk=pk)
    c_bands = Band.objects.filter(concerts__exact=c_concert)
    return render(
        request,
        'concert-detail.html',
        context = {
            'concert':c_concert,
            'bands':c_bands,
        },
    )


@login_required
def profile(request):
    c_user = request.user
    c_profile = c_user.profile

    return render(
        request,
        'profile.html',
        context = {
            'profile': c_profile,
            'c_user': c_user,
        },
    )


@permission_required('mediapleer.can_change', login_url='/')
def del_album(request, pk):
    c_album = Album.objects.get(pk=pk)
    if c_album :
        c_name = c_album.name
        Track.objects.filter(album__exact=c_album).delete()
        c_album.delete()
        return render(
            request,
            'album-del-suc.html',
            context = {
                'name':c_name,
            },
        )

@permission_required('mediapleer.can_change', login_url='/')
def del_track(request, pk):
    c_track = Track.objects.get(pk=pk)
    if c_track :
        c_name = c_track.name
        c_track.delete()
        return render(
            request,
            'track-del-suc.html',
            context = {
                'name':c_name,
            },
        )


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from mediapleer.forms import album_form

@permission_required('mediapleer.can_change', login_url='/')
def add_album(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = album_form(request.POST)
        # check whether it's valid:
        if form.is_valid():

            d_name = form.cleaned_data['name']
            d_desc = form.cleaned_data['description']
            d_band = form.cleaned_data['band']

            #f_band = Band.objects.get(pk=d_band)

            alb = Album(name=d_name, description=d_desc, band=d_band)
            alb.save()

            return HttpResponseRedirect(reverse('albums'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = album_form()

    return render(
        request,
        'album-add.html',
        {'form': form})


@permission_required('mediapleer.control_users', login_url='/')
def users(request):
    user_list = Profile.objects.all();
    return render(
        request,
        'users.html',
        context = {
            'user_list':user_list,
        },
    )

@permission_required('mediapleer.control_users', login_url='/')
def user(request, pk):
    c_profile = Profile.objects.get(pk=pk)
    c_user = c_profile.user

    return render(
        request,
        'profile.html',
        context = {
            'profile': c_profile,
            'c_user': c_user,
        },
    )

@permission_required('mediapleer.control_users', login_url='/')
def change_group(request, pk):
    c_profile = Profile.objects.get(pk=pk)
    c_user = c_profile.user

    if len(c_user.groups.all()) :
        c_user.groups.clear()
    else :
        c_group = Group.objects.get(name='moder')
        c_user.groups.add(c_group)

    return render(
        request,
        'profile.html',
        context = {
            'profile': c_profile,
            'c_user': c_user,
        },
    )
