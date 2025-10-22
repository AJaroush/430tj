from django.db import models

class Video(models.Model):
    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
    ]

    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=200)
    actor1_name = models.CharField(max_length=100)
    actor2_name = models.CharField(max_length=100, blank=True, null=True)
    director_name = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_year = models.IntegerField()

    def __str__(self):
        return self.movie_title
