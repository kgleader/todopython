from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookStore(models.Model):
    title = models.CharField(max_length=70, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=60, verbose_name='Подзаголовок')
    description = models.CharField(max_length=600, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    genre = models.CharField(max_length=60, verbose_name='Жанр')
    author = models.CharField(max_length=40, verbose_name='Автор')
    year = models.DateField(verbose_name='Год выхода книги')
    date = models.DateField(
        auto_now_add=True, verbose_name='Добавление книги на сайт')

    class Meta:
        verbose_name = 'Книжный маркет'
        verbose_name_plural = 'Книжные маркеты'
    