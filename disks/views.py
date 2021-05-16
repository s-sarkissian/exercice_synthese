from django.shortcuts import render
from django.http import Http404
from disks.models import Album
from disks.models import Track

# Create your views here.


def album(request):
    albums = Album.objects.all()
    return render(request, 'disks/album.html', {'albums_disponibles': albums})


def select(request, selected_id):
    try:
        albums = Album.objects.get(id=selected_id)
        tracks = Track.objects.get(album=selected_id)
    except Album.DoesNotExist:
        raise Http404

    return render(request, 'disks/track.html', {'album': albums}, {'track': tracks}),
