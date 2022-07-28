from django.shortcuts import render
from rest_framework import generics

from .models import Word
from .serializers import WordSerializer


class WordsApiView(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
