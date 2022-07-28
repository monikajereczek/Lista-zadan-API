from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import SimpleNote, Note, UrlNote, ListNoteDetails, ListNote

class SimpleNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleNote
        fields = '__all__'

class UrlNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlNote
        fields = '__all__'

class ListNoteSerializer2(serializers.Serializer):
    list_note = serializers.IntegerField(required=False)
    done = serializers.BooleanField(required=False)
    
    text = serializers.CharField(required=False, max_length=100)

class ListNoteSerializer3(serializers.Serializer):
    fields= ListNoteSerializer2


class ListNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNote
        fields = '__all__'

class ListDetailsNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNoteDetails
        fields = '__all__'

class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60, required=False)
    due_date = serializers.DateField(required=False)
    text_note = serializers.CharField(max_length=500, required=False)
    url_note = serializers.URLField(required=False)
    list_note = ListNoteSerializer3
