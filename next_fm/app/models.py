from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    login = models.CharField()
    password = models.CharField()
    role_id = models.IntegerField()


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    user_id = models.IntegerField()
    cover_id = models.IntegerField()
    artist_id = models.IntegerField()


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    album_id = models.IntegerField()
    duration = models.IntegerField()
    artist_id = models.IntegerField()


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    album_id = models.IntegerField()
    rating = models.IntegerField()
    created_at = models.DateField()


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    user_id = models.IntegerField()


class CollectionAlbum(models.Model):
    id = models.AutoField(primary_key=True)
    collection_id = models.IntegerField()
    album_id = models.IntegerField()


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    user_id = models.IntegerField()


class PlaylistSong(models.Model):
    id = models.AutoField(primary_key=True)
    playlist_id = models.IntegerField()
    song_id = models.IntegerField()


class AlbumGenre(models.Model):
    id = models.AutoField(primary_key=True)
    album_id = models.IntegerField()
    genre_id = models.IntegerField()


class SongGenre(models.Model):
    id = models.AutoField(primary_key=True)
    song_id = models.IntegerField()
    genre_id = models.IntegerField()


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    body = models.TextField()
    user_id = models.IntegerField()
    album_id = models.IntegerField()


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    picture_id = models.IntegerField()


class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    artist_id = models.IntegerField()