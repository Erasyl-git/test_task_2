from django.contrib import admin
from .models import BooksModel

class BooksAdmin(admin.ModelAdmin):
    #отображаем указанные данные в панеле администратора
    list_display = ['title', 'author', 'published_date', 'image']


admin.site.register(BooksModel, BooksAdmin)    
