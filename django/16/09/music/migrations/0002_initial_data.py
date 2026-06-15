# 0002_populate_music_data.py
# Generated using ChatGTP

import random
from django.db import migrations
import datetime

def add_music_data(apps, schema_editor):
    Artist = apps.get_model('music', 'Artist')
    Album = apps.get_model('music', 'Album')
    Song = apps.get_model('music', 'Song')

    # 아티스트 데이터
    artists_names = [
        "BTS", "BLACKPINK", "IU", "EXO", "TWICE", 
        "Red Velvet", "BIGBANG", "SEVENTEEN", "GOT7", "MAMAMOO", 
        "NCT", "ATEEZ", "Stray Kids", "MONSTA X", "GFRIEND", 
        "(G)I-DLE", "ITZY", "TXT", "DAY6", "LOONA"
    ]

    # 앨범 데이터 (가상의 앨범명)
    albums_titles = [
        "Dreamscape", "Neon Memories", "Eternal Summer", "Midnight Melody", "City Lights",
        "Moonlit Path", "Starry Horizon", "Heartbeat Symphony", "Whispers of Spring", "Dance in the Rain",
        "Sunset Boulevard", "Ocean Breeze", "Winter’s Tale", "Rhythmic Journey", "Beyond the Stars",
        "Echoes of Love", "Celestial Dance", "Mystic Nights", "Serenade of Youth", "Twilight Whisper"
    ]

    # 곡 데이터 (실제 곡명)
    songs_titles = [
        "Dynamite", "How You Like That", "Celebrity", "Love Shot", "Fancy",
        "Psycho", "Bang Bang Bang", "Left & Right", "Not By the Moon", "HIP",
        "Kick It", "Inception", "God’s Menu", "Love Killa", "MAGO",
        "Oh My God", "WANNABE", "Blue Hour", "Zombie", "Why Not?"
    ]

    artists = []
    for i, name in enumerate(artists_names, start=1):
        artist = Artist(
            name=name,
            image=f'artists/{str(i).zfill(4)}.jpg',
            description=f'{name} description'
        )
        artist.save()
        artists.append(artist)

    for i, (artist, album_title) in enumerate(zip(artists, albums_titles), start=1):
        album = Album(
            title=album_title,
            image=f'albums/{str(i).zfill(4)}.jpg',
            artist=artist,
            release_date=datetime.date.today(),
            genre='K-pop'
        )
        album.save()

        # 각 앨범에 5개의 노래 추가
        for j in range(random.randint(2, 10)):
            song_index = random.randint(0, len(songs_titles) - 1)
            Song(
                album=album,
                title=songs_titles[song_index],
                duration=datetime.timedelta(minutes=random.randint(1, 5), seconds=random.randint(0, 59))
            ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_music_data),
    ]