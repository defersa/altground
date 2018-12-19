from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.urls import reverse  # To generate URLS by reversing URL patterns

# Create your models here.


class City(models.Model):
	name = models.CharField(max_length = 200)
	def __str__(self):
		return self.name



class Concert(models.Model):
	name = models.CharField(max_length = 200)
	start = models.DateField(null = True)
	city = models.ForeignKey('City', on_delete = models.SET_NULL, null = True)

	def get_absolute_url(self):
		return reverse('concert-detail', args=[str(self.id)])

	def __str__(self):
		return self.name


class Genre(models.Model):
	"""
	Model representinf a music genre
	"""
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 1000)

	def get_absolute_url(self):
		return reverse('genre-detail', args=[str(self.id)])

	def __str__(self):
		return self.name



class Band(models.Model):

	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 1000)

	genre = models.ManyToManyField(Genre, blank=True)
	concerts = models.ManyToManyField(Concert, blank=True)

	def get_absolute_url(self):
		return reverse('band-detail', args=[str(self.id)])

	def __str__(self):
		return self.name


class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	concerts = models.ManyToManyField(Concert, blank=True)
	bands = models.ManyToManyField(Band, blank=True)	
	city = models.ForeignKey('City', on_delete = models.SET_NULL, null = True)

	class Meta:
		permissions = (("control_users", "Change group for users"),)

	def get_absolute_url(self):
		return reverse('user-detail', args=[str(self.id)])

	def __str__(self):
		return self.user.username 


class Album(models.Model):

	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 1000)

	band = models.ForeignKey('Band', on_delete = models.SET_NULL, null = True)

	def get_absolute_url(self):
		return reverse('album-detail', args=[str(self.id)])

	class Meta:
		permissions = (("can_change", "Delete or add albums"),)

	def __str__(self):
		return self.name



class Track(models.Model):

	name = models.CharField(max_length = 200)
	url = models.URLField(max_length = 200)

	album = models.ForeignKey('Album', on_delete = models.SET_NULL, null = True)
	feat = models.ManyToManyField(Band, blank=True)
	videos = models.ForeignKey('Video', on_delete = models.SET_NULL, null = True, blank=True)

	def get_absolute_url(self):
		return reverse('track-detail', args=[str(self.id)])


	def __str__(self):
		return self.name



class Video(models.Model):
	name = models.CharField(max_length = 200)
	url = models.URLField(max_length = 200)

	def get_absolute_url(self):
		"""Returns the url to access a particular book instance."""
		return reverse('ideo-detail', args=[str(self.id)])

	def __str__(self):
		return self.name


