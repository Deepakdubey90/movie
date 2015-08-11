from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import (list_route, detail_route)
from genre.models import Type
from ..serializers.genre import TypeSerializer
from django.utils import timezone
from django.contrib.sessions.models import Session


class TypeViewSet(viewsets.ModelViewSet):
    """
    List all type of movie.
    """
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
