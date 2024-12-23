# Generated by Django 5.1.1 on 2024-09-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=255, verbose_name='Рейс')),
                ('content', models.TextField(blank=True, verbose_name='Информация о рейсе')),
                ('city1', models.CharField(max_length=255, verbose_name='Город вылета')),
                ('city2', models.CharField(max_length=255, verbose_name='Город прибытия')),
                ('start_price', models.IntegerField(default=0, verbose_name='Начальная цена')),
                ('departure_date', models.DateTimeField(verbose_name='Дата вылета')),
                ('arrival_date', models.DateTimeField(verbose_name='Дата прибытия')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('photo', models.ImageField(default=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Информация о рейсах',
                'verbose_name_plural': 'Информация о рейсах',
                'ordering': ['-time_create'],
            },
        ),
    ]
