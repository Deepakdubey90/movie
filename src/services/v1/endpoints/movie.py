from rest_framework import viewsets
from utils import permissions
from rest_framework.response import Response
from movie.models import Movie
from ..serializers.movie import (MovieGetSerializer,
                                 MoviePostSerializer
                             )
from ..serializers.genre import TypeSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    List all type of movie.
    """
    permission_classes = (permissions.ReadAllWriteOnlyAdminPermission, )
    def get_serializer_class(self):
        serializer_class=MoviePostSerializer
        if self.request.method =='GET':
            serializer_class=MovieGetSerializer

        return serializer_class

    def get_queryset(self):
        movies = Movie.objects.filter(deleted_on__isnull=True)
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            movies = Movie.objects.filter(user_id=self.request.user.id)
        return movies
