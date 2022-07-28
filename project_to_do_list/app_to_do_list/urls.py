from django.urls import include, path
from .views import NoteView, SimpleNoteView, UrlNoteView, ListNoteView, ListDetailsNoteView, date_filter_view, home_view, status_filter_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


#router.register(r'Notes', NoteView, basename="Notes")
router.register(r'SimpleNotes', SimpleNoteView)
router.register(r'UrlNotes', UrlNoteView)
router.register(r'ListNotes', ListNoteView)
router.register(r'ListNotesDetails', ListDetailsNoteView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('notes/', NoteView.as_view(), name="Notatki"),
    path('filter_date/', date_filter_view, name="Filter"),
    path('filter_status/', status_filter_view, name="Filter"),
    path('', home_view, name="Home")
]