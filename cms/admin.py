from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Page, SiteConfig

admin.site.register(SiteConfig, SingletonModelAdmin)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated')
