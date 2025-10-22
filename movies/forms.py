from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'movie_title',
            'actor1_name',
            'actor2_name',
            'director_name',
            'movie_genre',
            'release_year',
        ]
