from django.contrib import admin
from .models import Album, Band, Concert, Genre, Track, Profile, Video, City

# Register your models here.

admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Concert)
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(City)