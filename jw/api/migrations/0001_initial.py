# Generated by Django 4.1.7 on 2023-03-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=29, verbose_name='названия')),
                ('auth', models.CharField(max_length=112, verbose_name='автор')),
                ('age', models.DateTimeField(verbose_name='год издания')),
                ('price', models.IntegerField(verbose_name='цена')),
            ],
        ),
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listname', models.CharField(max_length=40, verbose_name='имя списка')),
                ('allPrice', models.IntegerField(verbose_name='общая стоимость')),
                ('listBook', models.ManyToManyField(to='api.book', verbose_name='список книг')),
            ],
        ),
    ]
