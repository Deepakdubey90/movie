from django.contrib import admin
from movie.models import Movie


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, AuthorAdmin)
