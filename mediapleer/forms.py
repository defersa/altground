from django import forms
from .models import Album, Band, Concert, Genre, Track, Profile, Video, City

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.


class album_form(forms.Form):
    name = forms.CharField(label='Название альбома', max_length=200)
    description = forms.CharField(label='Описание', max_length=1000)
    band = forms.ModelChoiceField(label='Группа',queryset = Band.objects.all())

    def clean_name(self):
        d_name = self.cleaned_data['name']
        
        # Check date is not in past. 
        if d_name == '':
            raise ValidationError(_('Имя должно быть не пусто!'))

        return d_name


    def clean_description(self):
        d_desc = self.cleaned_data['description']
        
        # Check date is not in past. 
        if d_desc == '':
            raise ValidationError(_('Описание должно быть не пусто!'))

        return d_desc


    def clean_band(self):
        d_band = self.cleaned_data['band']
        
        # Check date is not in past. 
        if d_band == '':
            raise ValidationError(_('У альбома должна быть группа!'))

        return d_band