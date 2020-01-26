from django.db import models
from django.utils.safestring import mark_safe
from adminsortable.models import SortableMixin


class Photo(SortableMixin):
    image = models.ImageField(upload_to='gallery/%Y', verbose_name='Файл в формате (jpg, gif, png)')
    name = models.CharField(max_length=200, default='Фото', verbose_name='Название фото')
    photo_order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name='Сортировка')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['photo_order']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
        else:
            return mark_safe('<img src="https://via.placeholder.com/50" width="50" height="50" />')

    image_tag.short_description = 'Просмотр изображения'


class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    city = models.CharField(max_length=150, null=True, blank=True, verbose_name='Город')
    text = models.TextField(blank=True, null=True, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


class Booking(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя гостя')
    phone = models.CharField(max_length=150, verbose_name='Телефон гостя')
    email = models.EmailField(verbose_name='Email гостя')
    start_date = models.DateField(verbose_name='Дата заезда')
    end_date = models.DateField(verbose_name='Дата отъезда')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    persons = models.IntegerField(default=1, verbose_name='Количество человек')

    def __str__(self):
        return f'Заявка от {self.first_name} c {self.start_date} по {self.end_date}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['-created_at']
