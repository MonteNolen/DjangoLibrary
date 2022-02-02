# DjangoLibrary проект Notes
1.02.2022
 - Создал представления и формы для редактирования, создания, удаления постов.
 - Представления:
 - - RenewNoteStuff - дает возможность редактировать задачу по дате и тегу(маркеру). В дальнейшем переименую и перепишу.
 - - NoteCreate - для создания отчета.
 - - NoteUpdate - для редактирования отчета.
 - - NoteDelete - для удаления отчета.
 - Добавил возможность при создании отчета добавлять пользователя под которым был выполнен вход на сайт:
 
```Python
def form_valid(self, form):
        # создаем форму, но не отправляем ее в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.user = Author.objects.get(user=self.request.user)
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)
```
 - Разобрался с правами доступа по метке.
Важно:
Вместо <int:pk> нужно указать uuid, иначе выдает ошибку не соответствия id, пока не особо понял почему ;\
```Python
path('note/<uuid:pk>/renew/', views.RenewNoteStuff, name='renew-note-stuff')
```
До 1.02.2022
 - Создана модель автора отчета - Author, которая принимает зарегистрированного пользователя и в дальнейшем используется для создания отчетов. Костыль, так как пока не разобрался как полностью переопределять класс User под свои нужны, поэтому просто связываем User в модели Author, где выводим ФИО и дополнительные поля по необходимости.
 - Создана модель отчета - Note, которая выводит заголовок, дату создания, автора, поле для текста, теги.
 - Создана модель задач, для назначения ответственного за перенаправленный отчет - NoteInstance. Пока что криво-косо, в дальнейшем будет переписываться. Пока что просто для вида.
 - Создана модель для тегов. Для создания маркеров, для отображения важности задачи.

В представлениях описаны:
 - UserList - получает и выводит весь список пользователей.
 - UserDetailView - в будущем, возможно, понадобиться для вывода какой-то информации о пользователе.
 - NoteDetailView - выводит детальную информацию об отчете.
 - NoteListView - выводит информацию о всех отчетах.
 - TransmittedNotesByUserListView - выводит информацию пользователю о его задачах. Об отчете, который перенаправили на него.
 - index - главная страница
 - NoteListViewEditor - выводит информацию о всез задачах. Доступно только с определенными правами. В дальнейшем переименую.

