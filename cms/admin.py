from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from solo.admin import SingletonModelAdmin
from .models import Page, SiteConfig, Menu, MenuItem
from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric
from adminsortable.admin import SortableAdmin, SortableGenericTabularInline

admin.site.register(SiteConfig, SingletonModelAdmin)


class MenuItemsGeneric(GenericTabularInline):
    model = MenuItem
    extra = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'home', 'slug', 'created', 'updated')
    inlines = (MenuItemsGeneric,)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'template')
        }),
        ('SEO настройки', {
            'classes': ('wide',),
            'fields': ('meta_title', 'meta_description', 'slug'),
        }),
    )

    def home(self, obj):
        return True if obj.is_front else False

    home.short_description = 'Главная страница'
    home.boolean = True


class MenuItemInlines(TabularInlineWithGeneric):
    extra = 1
    model = MenuItem


@admin.register(Menu)
class MenuAdmin(GenericAdminModelAdmin):
    inlines = (MenuItemInlines,)
    content_type_whitelist = ('cms/page',)


@admin.register(MenuItem)
class MenuItemAdmin(SortableAdmin):
    list_display = ['name', 'menu', ]
