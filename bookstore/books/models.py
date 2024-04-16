from django.db import models


class BooksModel(models.Model):
    #у нас тут есть поля для заголовка, описание, изображение книги,автора и даты пуликации
    title = models.CharField(max_length=50, verbose_name='Название книги')
    content = models.TextField(verbose_name='Описание')
    author = models.CharField(max_length=50, verbose_name='Имя автора')
    published_date = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(upload_to='book_images/', verbose_name='Изображение книги', blank=True, null=True)

    def __str__(self):
        return f'Название книги {self.title}'
