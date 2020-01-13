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
    maintenance_mode = models.BooleanField(default=False, verbose_name='Режим обслуживания')
    front_page = models.OneToOneField('Page', blank=True, null=True, verbose_name='Главная страница',
                                      on_delete=models.SET_NULL)
    logo = models.FileField(upload_to='site/', blank=True, null=True, verbose_name='Логотип')
    favicon = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name='Значок сайта')

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
        ('side', 'Боковое меню'),
        ('footer', 'Подвал'),
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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Тип контента')
    object_id = models.PositiveIntegerField(verbose_name='ID обьекта')
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'