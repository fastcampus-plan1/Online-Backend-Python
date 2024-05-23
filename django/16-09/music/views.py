from django.shortcuts import render
from django.db.models import Count, Sum, Min, Max, Avg, StdDev, Variance

from music.models import Artist, Album, Song
from django.shortcuts import get_object_or_404

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist-list.html', {'artists': artists})

def artist_detail(request, id):
    artist = get_object_or_404(Artist, id=id)
    return render(request, 'artist-detail.html', {'artist': artist})

def albums_list(request):
    albums = Album.objects.annotate(
        song_count=Count('songs'),  # 곡 수
        average_song_duration=Avg('songs__duration'),   # 평균 곡 길이
        longest_song_duration=Max('songs__duration'),   # 가장 긴 곡 길이
        total_duration=Sum('songs__duration')        # 총 곡 길이
    )
    return render(request, 'album-list.html', {'albums': albums})

def albums_detail(request, id):
    album = get_object_or_404(Album, id=id)
    return render(request, 'album-detail.html', {'album': album})

def statistics_view(request):
    statistics = Album.objects.aggregate(
        album_count=Count('id'),  # 앨범 수
        earliest_release=Min('release_date'),  # 가장 이른 발매일
        latest_release=Max('release_date'),  # 가장 늦은 발매일
        total_songs=Sum('songs__id'),  # 총 곡 수
        average_duration=Avg('songs__duration'),  # 평균 곡 길이
        duration_stddev=StdDev('songs__duration'),  # 곡 길이의 표준 편차
        duration_variance=Variance('songs__duration')  # 곡 길이의 분산
    )
    return render(request, 'statistics.html', {'statistics': statistics})
