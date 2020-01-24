from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(SortableAdmin):
    list_display = ['name', 'image_tag', ]
