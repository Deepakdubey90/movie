from django.conf.urls import patterns, url,include
from rest_framework import routers
from .endpoints import (movie,
                        genre,
                        user,
                    )

router = routers.DefaultRouter()
router.register(r'user',  user.UserDetailViewSet, base_name="user")
router.register(r'movie', movie.MovieViewSet, base_name="movie")
router.register(r'genre', genre.TypeViewSet, base_name="genre")

urlpatterns = [
    url(r'^user/auth', user.AuthUserViewSet.as_view()),
    #url(r'auth/login/$', user.LoginView.as_view(), name='login'),
    url(r'^user/me', user.MeViewSet.as_view()),
    url(r'authentication/', include('rest_framework.urls',
                                    namespace='rest_framework')),
    url(r'^', include(router.urls))
]
