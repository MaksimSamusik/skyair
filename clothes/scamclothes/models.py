from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Planes(models.Model):
    flight = models.CharField(max_length=255, verbose_name='Рейс')
    content = models.TextField(blank=True, verbose_name='Информация о рейсе')
    city1 = models.CharField(max_length=255, verbose_name='Город вылета')
    city2 = models.CharField(max_length=255, verbose_name='Город прибытия')
    start_price = models.IntegerField(default=0, verbose_name='Начальная цена')
    departure_date = models.DateTimeField(verbose_name='Дата вылета')
    arrival_date = models.DateTimeField(verbose_name='Дата прибытия')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=True, verbose_name='Фото')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.flight

    def get_absolute_url(self):
        return reverse('flight_post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_create']
        verbose_name = "Информация о рейсах"
        verbose_name_plural = "Информация о рейсах"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user/%Y/%m/d', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Bucket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BucketItem(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    plane = models.ForeignKey(Planes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)
