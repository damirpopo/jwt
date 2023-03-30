from django.db import models


class Book(models.Model):
    name=models.CharField(max_length=29,verbose_name='названия')
    auth=models.CharField(max_length=112,verbose_name='автор')
    age=models.DateTimeField(verbose_name='год издания')
    price=models.IntegerField(verbose_name='цена')

    def __str__(self):
        return self.name

class OrderBook(models.Model):
    listname=models.CharField(max_length=40,verbose_name='имя списка')
    listBook=models.ManyToManyField(Book,verbose_name='список книг')
    allPrice=models.IntegerField(verbose_name='общая стоимость')