from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('notes', views.NoteListView.as_view(), name='notes'),
    path('users', views.UserList, name='users'),
    path('note-editor', views.NoteListViewEditor.as_view(), name='note-editor'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('mynotes', views.TransmittedNotesByUserListView.as_view(), name='my-borrowed'),
]