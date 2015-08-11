from rest_framework import serializers
from genre.models import Type


class TypeSerializer(serializers.ModelSerializer):
    """To serialize Type. """

    id = serializers.ReadOnlyField()

    class Meta:
        model = Type
        fields = ('id', 'slug', 'genre')
