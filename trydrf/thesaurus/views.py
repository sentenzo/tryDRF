from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Language, Word
from .serializers import WordSerializer


class WordsApiView(APIView):
    def get(self, request):
        words = Word.objects.all().values()
        return Response({"words": words})

    def post(lf, request):
        langs = {"en": "English", "ru": "Русский"}
        # fmt: off
        new_word = Word.objects.create(
            spelling= request.data['spelling'],  # "apple", 
            ipa_transcription = request.data['ipa_transcription'],
            definition = request.data['definition'],
            language = Language.objects.get(
                name=langs[request.data["language_code"]]
            ),
        )
        # fmt: on

        return Response({"word": model_to_dict(new_word)})


# class WordsApiView(generics.ListAPIView):
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer
