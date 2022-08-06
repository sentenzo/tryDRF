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
        return Response({"words": WordSerializer(words, many=True).data})

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"word": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk field is required"})

        try:
            instance = Word.objects.get(pk=pk)
        except:
            return Response({"error": f"Feild to find the object (pk={pk}"})

        serializer = WordSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"word": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk field is required"})

        try:
            instance = Word.objects.get(pk=pk)
        except Exception as ex:
            return Response({"error": f"Feild to find the object (pk={pk})"})

        instance.delete()

        return Response({"word": f"deleted post (pk={pk})"})


# class WordsApiView(generics.ListAPIView):
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer
