from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users', views.UserList, name='users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('notes', views.NoteListView.as_view(), name='notes'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('all-tasks', views.TaskListView.as_view(), name='all-tasks'),
    path('mytasks', views.MyTaskView.as_view(), name='my-tasks'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    
    # path('note/<int:pk>/renew/', views.RenewNoteDateTask, name='renew-note-date-task'),
    # re_path(r'^note/(?P<pk>[-\w]+)/renew/$', views.RenewNoteStuff, name='renew-note-stuff'),
    path('note/create/', views.NoteCreate.as_view(), name='note-create'),
    path('<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
    path('add-task', views.TaskCreateView.as_view(), name='add-task'),
    ]