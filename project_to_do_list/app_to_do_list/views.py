from rest_framework.response import Response
from .models import Note, SimpleNote, UrlNote, ListNoteDetails, ListNote
from .serializers import  NoteSerializer, SimpleNoteSerializer, UrlNoteSerializer, ListNoteSerializer, ListDetailsNoteSerializer
from rest_framework import viewsets, mixins
import itertools
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic.edit import FormView
from .forms import FilterForm, StatusFiler
from django.shortcuts import render
from datetime import date

class NoteView(APIView):
    serializer_class = NoteSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app_to_do_list/notes.html'

    def get(self, request):
        q1 = SimpleNote.objects.all() 
        q2 = UrlNote.objects.all()
        q3 = ListNote.objects.all()
        q4= ListNote.objects.none()
        for note in q3:
            q4=itertools.chain(q4, ListNote.objects.filter(note_ptr_id= note.note_ptr_id))
            q4=itertools.chain(q4, ListNoteDetails.objects.filter(list_note_id = note))
        return Response({'sn': q1, 'un':q2, 'ln':q4})

  

class SimpleNoteView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SimpleNote.objects.all() 
    serializer_class = SimpleNoteSerializer

def date_filter_view(request):
    context={}
    if request.method == "POST":
        form=FilterForm(request.POST or None)
        if form.is_valid():
            data_od=request.POST.get('Start_date')
            data_do=request.POST.get('End_date')
            print(data_od)
            q1 = Note.objects.filter(due_date__range = (data_od, data_do))
            context = {'notes':q1}
            return render(request, 'app_to_do_list/filter.html', context)
    form = FilterForm()
    return render(request, 'app_to_do_list/filter.html', {'form':form})

def status_filter_view(request):
    context={}
    if request.method == "POST":
        form=StatusFiler(request.POST or None)
        if form.is_valid():
            status=request.POST.get('Status')
            print(status)
            if status == '1':
                q1 = Note.objects.filter(due_date__lt = date.today())
                print(date.today())
                context = {'notes':q1}
            if status == '2':
                q1 = Note.objects.filter(due_date__gt = date.today())
                context = {'notes':q1}
            if status == '3':
                q1 = Note.objects.filter(due_date__isnull = True)
                context = {'notes':q1}
            return render(request, 'app_to_do_list/filter.html', context)
    form = StatusFiler()
    return render(request, 'app_to_do_list/filter.html', {'form':form})   
    
def home_view(request):
    urls = {'See all notes':'http://127.0.0.1:8000/notes/',
     'Filter by date':'http://127.0.0.1:8000/filter_date/',
     'Filter by status':'http://127.0.0.1:8000/filter_status',
     'Create notes':'http://127.0.0.1:8000/api/'}
    return render(request, 'app_to_do_list/home.html', {'urls':urls})       

  
class UrlNoteView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UrlNote.objects.all()
    serializer_class = UrlNoteSerializer

class ListDetailsNoteView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ListNoteDetails.objects.all()
    serializer_class = ListDetailsNoteSerializer

class ListNoteView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ListNote.objects.all()
    serializer_class = ListNoteSerializer
