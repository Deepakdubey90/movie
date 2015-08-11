from django.conf.urls import include, url

urlpatterns = [
    url(r'^v1/', include('services.v1.urls', namespace='services.v1')),
]
