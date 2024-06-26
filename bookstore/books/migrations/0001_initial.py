# Generated by Django 5.0.1 on 2024-04-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название книги')),
                ('content', models.TextField(verbose_name='Описание')),
                ('author', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('published_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
