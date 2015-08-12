from django.conf.urls import include, url
from django.contrib import admin
from .views import IndexView
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
import os


document_root = os.path.join(
    settings.BASE_DIR, '..', '..', 'static'
) if settings.DEBUG else settings.STATIC_ROOT

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^api/', include('services.urls', namespace='services')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': document_root}),
]
