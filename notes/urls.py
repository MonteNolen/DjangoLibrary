from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes', views.NoteListView.as_view(), name='notes'),
    path('users', views.UserList, name='users'),
    path('all-tasks', views.NoteListViewEditor.as_view(), name='all-tasks'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('task/<uuid:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('mytasks', views.TransmittedNotesByUserListView.as_view(), name='my-tasks'),
    path('note/<uuid:pk>/renew/', views.RenewNoteDateTask, name='renew-note-date-task'),
    # re_path(r'^note/(?P<pk>[-\w]+)/renew/$', views.RenewNoteStuff, name='renew-note-stuff'),
    path('note/create/', views.NoteCreate.as_view(), name='note-create'),
    path('<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
]