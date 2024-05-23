
from django.http import JsonResponse

from music.models import Album


def albums_list(request):
    albums = list(Album.objects.values("id", "title"))
    data = []
    for song in albums:
        data.append({
            'id': song['id'],
            'title': song['title'],
        })
    return JsonResponse({'albums': data}, safe=False)
