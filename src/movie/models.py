from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from genre.models import Type
from django.contrib.auth import get_user_model


class Movie(models.Model):

    popularity = models.DecimalField(
        _('Popularity'), decimal_places=6, max_digits=20,
        null=True, blank=True, default=None
    )
    director = models.CharField(
        _('Director'), max_length=40, blank=False, null=True
    )
    imdb_score = models.DecimalField(
        _('IMDB Score'), decimal_places=6, max_digits=20,
        null=True, blank=True, default=None
    )
    name = models.CharField(
        _('Name'), max_length=30, blank=False, null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'),
        null=True
    )
    genre = models.ManyToManyField(Type, blank=True)
    deleted_on = models.DateTimeField(
        'Deleted On', null=True, blank=True, default=None
    )

    def __str__(self):
        return self.name
