from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('notes', views.NoteListView.as_view(), name='notes'),
    path('users', views.UserList, name='users'),
    path('note-editor', views.NoteListViewEditor.as_view(), name='note-editor'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('mynotes', views.TransmittedNotesByUserListView.as_view(), name='my-borrowed'),
    path('note/<uuid:pk>/renew/', views.RenewNoteStuff, name='renew-note-stuff'),
    # re_path(r'^note/(?P<pk>[-\w]+)/renew/$', views.RenewNoteStuff, name='renew-note-stuff'),
    path('note/create/', views.NoteCreate.as_view(), name='note-create'),
    path('<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
]