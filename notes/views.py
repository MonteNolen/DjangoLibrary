from django.shortcuts import render, get_object_or_404
from .models import Note, Tags, NoteInstance, Author
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
#from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from .forms import RenewNoteForm


# class UserListView(generic.ListView):
#     model = Author
#     template_name = 'notes/users.html'
#     #context_object_name = 'authors_list'

def UserList(request):
    users_list = Author.objects.all()

    context = {
            "title": "Список пользователей",
            "users_list": users_list,
        }
    return render(request, 'notes/users.html', context)

class UserDetailView(generic.DetailView):
    model = User
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
    paginate_by = 10


class TransmittedNotesByUserListView(LoginRequiredMixin,generic.ListView):
    # Общее представление на основе классов, в котором перечислены книги, предоставленные текущему пользователю
    model = NoteInstance
    template_name ='notes/noteinstance_list_borrowed_user.html'
    paginate_by = 2

    def get_queryset(self):
        return NoteInstance.objects.filter(responsible=self.request.user).filter(status__exact='В работе').order_by('must_do')


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


class NoteListViewEditor(PermissionRequiredMixin, generic.ListView):
    model = NoteInstance
    permission_required = 'notes.can_mark_returned'
    template_name = 'notes/note_editor.html'
    paginate_by = 10
    def get_queryset(self):
        return NoteInstance.objects.all()

@permission_required('notes.can_mark_returned')
def RenewNoteStuff(request, pk):
    note_inst = get_object_or_404(NoteInstance, pk=pk)

    # Если данный запрос типа POST, тогда
    if request.method == 'POST':

        # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = RenewNoteForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            #(здесь мы просто присваиваем их полю must_do)
            note_inst.must_do = form.cleaned_data['must_do']
            note_inst.save()

            return HttpResponseRedirect(reverse('note-editor') )

    # Если это GET (или какой-либо ещё), создать форму по умолчанию.
    else:
        proposed_must_do = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewNoteForm(initial={'must_do': proposed_must_do,})

    return render(
        request, 
        'notes/renew_note_stuff.html', 
        context = {
            'form': form,
            'noteinst':note_inst
            }
        )



    """
    Работа с формами
    """

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    #fields = '__all__'
    fields = ['title', 'date', 'textarea', 'tags']
    success_url = reverse_lazy('notes')
    raise_exception = True
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(NoteCreate, self).form_valid(form)
    def form_valid(self, form):
        # создаем форму, но не отправляем ее в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.user = Author.objects.get(user=self.request.user)
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'date', 'textarea', 'tags']
    success_url = reverse_lazy('notes')

class NoteDelete(PermissionRequiredMixin, DeleteView):
    model = Note
    permission_required = 'notes.can_mark_returned'
    success_url = reverse_lazy('notes')
