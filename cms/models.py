from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from solo.models import SingletonModel
from tinymce import HTMLField
from uuslug import uuslug


class SiteConfig(SingletonModel):
    site_name = models.CharField(max_length=255, default='Мой сайт', verbose_name='Название сайта')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Телефон')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    maintenance_mode = models.BooleanField(default=False, verbose_name='Режим обслуживания')
    front_page = models.OneToOneField('Page', blank=True, related_name='is_front', null=True,
                                      verbose_name='Главная страница',
                                      on_delete=models.SET_NULL)
    logo = models.FileField(upload_to='site/', blank=True, null=True, verbose_name='Логотип')
    favicon = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name='Значок сайта')
    footer = HTMLField(blank=True, null=True, verbose_name='Футер')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Настройки'


class SEOBase(models.Model):
    meta_title = models.CharField(max_length=150, verbose_name='Мета заголовок')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')
    slug = models.SlugField(verbose_name='ЧПУ ссылка', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.meta_title, instance=self)
        super(SEOBase, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Page(SEOBase):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cms:page', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Menu(models.Model):
    POSITON_CHOICES = (
        (None, 'Выберите позицию'),
        ('main', 'Главное меню'),
    )
    name = models.CharField(max_length=200, verbose_name='Название меню')
    position = models.CharField(max_length=100, choices=POSITON_CHOICES, unique=True, db_index=True,
                                verbose_name='Позиция')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name='Меню')
    name = models.CharField(max_length=200, verbose_name='Название')
    parent = models.ForeignKey('self', related_name='childs', blank=True, null=True, on_delete=models.SET_NULL,
                               verbose_name='Родитель')
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name='Произвольная ссылка')
    content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name='Тип контента')
    object_id = models.PositiveIntegerField(blank=True, null=True, verbose_name='ID обьекта')
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name

    def get_link(self):
        if self.content_object:
            return self.content_object.get_absolute_url()
        elif self.link:
            return self.link
        else:
            return '#'

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
