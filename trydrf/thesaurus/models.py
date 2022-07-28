from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Word(models.Model):
    spelling = models.CharField(max_length=255)
    ipa_transcription = models.CharField(max_length=255, null=True, blank=True)
    definition = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.spelling
