from django.urls import path
from .views import *


urlpatterns = [
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/',BookDetailView.as_view(), name='book_detail'),
    path('add_book/', BookAddView.as_view(), name='book_add'),
    path('search/', search_books, name='search_books')

]