from django import forms
from .models import BooksModel

#создаем форму для ввода данных о книге 
class CreateBookForm(forms.ModelForm):
    #поле для ввода названия книги 
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Добавить название книги', 'class': 'form-control'}
        )
    )
    #поле для ввода описания книги 
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Добавить описание', 'class': 'form-control'}
        )
    )
    #поле для ввода автора
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Добавить имя автора', 'class': 'form-control'}
        )
    )
    #поле для ввода даты создания книги
    published_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'placeholder': 'год-мес.-день', 'class': 'form-control'}
        )
    )
    #поле для изображение книги
    image = forms.ImageField(label='Изображение книги')


    #изменяем поведение класса с помощью метакласса
    class Meta:
        model = BooksModel
        fields = ['title', 'content', 'author', 'published_date', 'image']
