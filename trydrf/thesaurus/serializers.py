import io
from operator import mod
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Word


# class WordModel:
#     def __init__(self, spelling, definition) -> None:
#         self.spelling = spelling
#         self.definition = definition


class WordSerializer(serializers.Serializer):
    spelling = serializers.CharField(max_length=255)
    ipa_transcription = serializers.CharField(max_length=255)
    definition = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    language_id = serializers.IntegerField()

    def create(self, validated_data):
        return Word.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        instance.spelling = validated_data.get("spelling", instance.spelling)
        instance.ipa_transcription = validated_data.get(
            "ipa_transcription", instance.ipa_transcription
        )
        instance.definition = validated_data.get("definition", instance.definition)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.language_id = validated_data.get("language_id", instance.language_id)

        instance.save()

        return instance


# def encode():
#     model = WordModel("123456", "table is a table")
#     model_sr = WordSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#     print()


# def decode():
#     stream = io.BytesIO(
#         b"""{
#         "spelling": "test000",
#         "ipa_transcription": "/test/",
#         "definition": "a way of discovering, by questions or practical activities, what someone knows, or what someone or something can do or is like"
#     }"""
#     )

#     data = JSONParser().parse(stream)
#     serializer = WordSerializer(data=data)

#     # serializer.is_valid()

#     print(serializer.is_valid())
#     print(serializer.validated_data)
#     print()


# encode()
# decode()
