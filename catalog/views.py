from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/authors.html'
    #context_object_name = 'authors_list'

class AuthorDetailView(generic.DetailView):
    model = Author

class BookDetailView(generic.DetailView):
    model = Book

class BookListView(generic.ListView):
    model = Book
    #context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'catalog/book_list.html'  # Определение имени вашего шаблона и его расположения
    #def get_queryset(self):
        #return Book.objects.filter(title__icontains='Хоббит')[:5] # Получить 5 книг, содержащих 'war' в заголовке
    paginate_by = 2

def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_genres = Genre.objects.count()

    # Книги с названием Хоббит, или Туда и обратно
    # test
    num_books_word = Book.objects.filter(title='Хоббит, или Туда и обратно').count()

    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context  
    return render(
        request,
        'catalog/index.html',
        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_word': num_books_word,
            'title': 'Главная страница',
            'num_visits': num_visits}
    )

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    # Общее представление на основе классов, в котором перечислены книги, предоставленные текущему пользователю
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')