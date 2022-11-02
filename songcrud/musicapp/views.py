from django.shortcuts import render
from rest_framework import viewsets
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
# Create your views here.
class ArtisteView(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class LyricView(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer