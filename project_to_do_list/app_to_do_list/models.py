from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.core.exceptions import ValidationError

class Note(models.Model):
    title = models.CharField(max_length=60)
    due_date = models.DateField(blank=True, null=True)

class SimpleNote(Note):
    text_note = models.CharField(max_length=500, blank=True, default = None)

class UrlNote(Note):
    url_note = models.URLField(max_length=500,  blank=True, null=True, default = None)

class ListNote(Note):
    pass

class ListNoteDetails(models.Model):
    list_note= models.ForeignKey(ListNote, on_delete=models.CASCADE, related_name='notes')
    done = models.BooleanField()
    text = models.CharField(max_length=100, blank=True, default = None)
