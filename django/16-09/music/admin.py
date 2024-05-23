from django.contrib import admin

from music.models import Album, Artist, Song

# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    list_display_links = ('name', 'image')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'artist', 'release_date', 'genre')
    list_display_links = ('title', 'image')
    search_fields = ('title', 'genre')
    list_filter = ('title', 'genre')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('album', 'title', 'duration')
    list_display_links = ('album', 'title')
    search_fields = ('title',)
    list_filter = ('title',)

