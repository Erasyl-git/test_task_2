# Generated by Django 5.0.1 on 2024-04-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/', verbose_name='Изображение книги'),
        ),
    ]
