from django.views.generic import ListView, DetailView, CreateView
from .models import BooksModel
from django.shortcuts import get_object_or_404, render
from typing import Union
from django.http import HttpRequest
from .forms import CreateBookForm
from django.urls import reverse_lazy


#выводим список данных с базы данных
class BookListView(ListView):
    model = BooksModel
    #указываем путь к шаблону списку книг
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'


#выводим всю информацию о книгах
class BookDetailView(DetailView):

    queryset = BooksModel.objects.all()

    #используются аннотации чтобы понять что каждый аргумент в себе принимает
    def get(self, request:HttpRequest, pk:int) -> Union[str, int]:
        #получаем книгу по первичному ключу, в ином случае возвращаем 404
        book = get_object_or_404(self.queryset, pk=pk)

        #рендер шаблона с подробной информации о книге
        return render(request, 'books/book_detail.html', 
                      {'book_detail': book})

#добавление книги
class BookAddView(CreateView):

    model = BooksModel
    #путь к шаблону создании книг
    template_name = 'books/book_add.html'

    #указываем форму для создание книги
    form_class = CreateBookForm

    #после успешного создания книги нас перенаправляет на страницу списка книг
    success_url = reverse_lazy('book_list')


# Функция для поиска книг по запросу пользователя
def search_books(request):

    #получаем запрос пользователя из параметров url
    query = request.GET.get('query')
    #если запрос пользователя был передан, то ищем енигу с соответствующим заголовком (title)
    if query:
        search_results = BooksModel.objects.filter(title__icontains=query)

    #иначе возвращаем пустые данные
    else:
        search_results = None

    #рендерим наш результат
    return render(request, 'books/book_detail.html', {'search_results': search_results, 'query': query})

