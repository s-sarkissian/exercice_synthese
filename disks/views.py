from django.shortcuts import render
from django.http import Http404
from .models import Album


# Create your views here.


def album(request):
    albums = Album.objects.all()
    return render(request, 'disks/album.html', {'albums_disponibles': albums})


def select(request, id):
    try:
        albums = Album.objects.get(id=id)
    except Album.DoesNotExist:
        raise Http404

    return render(request, 'disks/album.html', {'album': albums}),
