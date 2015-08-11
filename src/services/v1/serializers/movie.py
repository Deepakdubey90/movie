from rest_framework import serializers
from movie.models import Movie
from genre.models import Type
from django.contrib.auth import get_user_model
from ..serializers.genre import TypeSerializer
User = get_user_model()


class MovieGetSerializer(serializers.ModelSerializer):
    """To serialize Movie for GET. """

    id = serializers.ReadOnlyField()
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return [g.genre for g in obj.genre.all()] if obj.genre else []

    class Meta:
        model = Movie
        fields = ('id', 'popularity', 'director', 'imdb_score', 'name', 'genres',)


class MoviePostSerializer(serializers.ModelSerializer):
    """To serialize Movie for POST. """

    id = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        field = ('id', 'popularity', 'director', 'imdb_score', 'name', 'genre',)
        exclude = ('deleted_on', 'user',)
