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
    text = models.TextField(blank=True, null=True, verbose_name='Отзыв')

    def __str__(self):
        return self.name