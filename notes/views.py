from django.shortcuts import render
from .models import Note, Tags, NoteInstance, Author
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class UserListView(generic.ListView):
    model = Author
    template_name = 'notes/users.html'
    ##context_object_name = 'authors_list'

class UserDetailView(generic.DetailView):
    model = Author
    template_name = 'notes/user_detail.html'

class NoteDetailView(generic.DetailView):
    model = Note

class NoteListView(generic.ListView):
    model = Note
    #context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'notes/note_list.html'  # Определение имени вашего шаблона и его расположения
    #def get_queryset(self):
        #return Book.objects.filter(title__icontains='Хоббит')[:5] # Получить 5 книг, содержащих 'war' в заголовке
    paginate_by = 2

class TransmittedNotesByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    # Общее представление на основе классов, в котором перечислены книги, предоставленные текущему пользователю
    model = NoteInstance
    template_name ='notes/noteinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return NoteInstance.objects.filter(borrower=self.request.user).filter(status__exact='В работе').order_by('due_back')


def index2(request):
    num_notes = Note.objects.all().count()
    num_instances = NoteInstance.objects.all().count()
    # Заявки со статусом "Открыто"
    num_instances_open = NoteInstance.objects.filter(status__exact='Открыто').count()


    return render(
        request,
        'notes/index.html',
        context = {
            'num_notes': num_notes,
            'num_instances': num_instances,
            'num_instances_open': num_instances_open,
            'title': 'Главная страница',
            }
    )