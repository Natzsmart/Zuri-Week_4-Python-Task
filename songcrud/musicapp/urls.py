#from operator import index
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('artistes', views.ArtisteView)
router.register('songs', views.SongView)
router.register('lyrics', views.LyricView)

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include(router.urls))
]