from django.contrib import admin
from models import Role, User, Album, Song, Genre, Rating, Collection, CollectionAlbum, Playlist, PlaylistSong, AlbumGenre, SongGenre, Review, Artist, Favorite

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Collection)
admin.site.register(CollectionAlbum)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
admin.site.register(AlbumGenre)
admin.site.register(SongGenre)
admin.site.register(Review)
admin.site.register(Artist)
admin.site.register(Favorite)
