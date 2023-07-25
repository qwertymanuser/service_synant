from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    synonyms = models.JSONField(default=list, blank=True, null=True, help_text="JSON array of synonyms.")
    antonyms = models.JSONField(default=list, blank=True, null=True, help_text="JSON array of antonyms.")

    def __str__(self):
        return self.word
