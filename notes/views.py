from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime

# from .forms import RenewTaskForm
from .models import Note, Task, Author


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

class TaskDetailView(generic.DetailView):
    model = Task

class NoteListView(generic.ListView):
    model = Note
    #context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'notes/note_list.html'  # Определение имени вашего шаблона и его расположения
    #def get_queryset(self):
        #return Book.objects.filter(title__icontains='Хоббит')[:5] # Получить 5 книг, содержащих 'war' в заголовке
    paginate_by = 10


class MyTaskView(LoginRequiredMixin,generic.ListView):
    model = Task
    template_name ='notes/my_task.html'
    paginate_by = 2

    def get_queryset(self):
        # return Task.objects.filter(responsible=self.request.user).filter(status__exact='Открыт').order_by('created')
        return Task.objects.filter(user=Author.objects.get(user=self.request.user)).order_by('created')


def index(request):
    # num_notes = Note.objects.all().count()
    # num_tasks = Task.objects.all().count()
    # num_tasks_open = Task.objects.filter(status__exact='Открыто').count()
    return render(
        request,
        'notes/index.html',
        context = {
            # 'num_notes': num_notes,
            # 'num_tasks': num_tasks,
            # 'num_tasks_open': num_tasks_open,
            'title': 'Главная страница',
            }
    )


class TaskListView(PermissionRequiredMixin, generic.ListView):
    model = Task
    permission_required = 'notes.can_mark_returned'
    template_name = 'notes/all_tasks.html'
    paginate_by = 10
    def get_queryset(self):
        return Task.objects.all()

# @permission_required('notes.can_mark_returned')
# def RenewNoteDateTask(request, pk):
#     note_task = get_object_or_404(Task, pk=pk)

#     # Если данный запрос типа POST, тогда
#     if request.method == 'POST':

#         # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
#         form = RenewTaskForm(request.POST)

#         # Проверка валидности данных формы:
#         if form.is_valid():
#             # Обработка данных из form.cleaned_data
#             #(здесь мы просто присваиваем их полю closed)
#             note_task.closed = form.cleaned_data['closed']
#             note_task.save()

#             return HttpResponseRedirect(reverse('all-tasks') )

#     # Если это GET (или какой-либо ещё), создать форму по умолчанию.
#     else:
#         proposed_closed = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewTaskForm(initial={'closed': proposed_closed,})

#     return render(
#         request, 
#         'notes/renew_note_date_task.html', 
#         context = {
#             'form': form,
#             'notetask':note_task
#             }
#         )

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    #fields = '__all__'
    fields = ['title', 'textarea']
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
    fields = ['title', 'textarea']
    success_url = reverse_lazy('notes')

class NoteDelete(PermissionRequiredMixin, DeleteView):
    model = Note
    permission_required = 'notes.can_mark_returned'
    success_url = reverse_lazy('notes')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

class TaskCreateView(CreateView):
    model = Task
    template_name = 'notes/add_task.html'
    fields = ['title', 'textarea']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = Author.objects.get(user=self.request.user)
        fields.save()
        return super().form_valid(form)