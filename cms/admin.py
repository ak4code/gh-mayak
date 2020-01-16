from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Page, SiteConfig, Menu, MenuItem
from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric

admin.site.register(SiteConfig, SingletonModelAdmin)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'home', 'slug', 'created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
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
