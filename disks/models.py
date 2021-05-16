from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200),
    id = models.BigIntegerField(),

    class Meta:
        ordering = ['id']
        verbose_name = 'artist'

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200),
    id = models.IntegerField(),
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'album'

    def __str__(self):
        return self.title


class Track(models.Model):
    id = models.IntegerField(),
    name = models.CharField(max_length=200),
    composer = models.CharField(max_length=200),
    milliseconds = models.IntegerField(),
    bytes = models.IntegerField(),
    unitPrice = models.DecimalField(),
    album = models.ForeignKey(Album, on_delete=models.SET_NULL),

    class Meta:
        ordering = ['id']
        verbose_name = 'track'

    def __str__(self):
        return self.name
