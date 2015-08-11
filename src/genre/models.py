from django.db import models
from django.utils.translation import ugettext_lazy as _


class Type(models.Model):

    slug = models.SlugField(
        _('Slug'), max_length=16, db_index=True
    )
    genre = models.CharField(
        _('Genre'), max_length=16, db_index=True
    )

    def __str__(self):
        return self.genre
