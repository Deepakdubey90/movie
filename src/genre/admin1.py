from django.contrib import admin
from genre.models import Type


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, AuthorAdmin)
