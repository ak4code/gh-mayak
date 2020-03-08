from django.contrib import sitemaps
from django.urls import reverse

from cms.models import Page


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['cms:home', 'hotel:photos', 'hotel:feedback']

    def location(self, item):
        return reverse(item)


class PageSitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Page.objects.filter(is_front=None)

    def lastmod(self, obj):
        return obj.updated


sitemaps = {
    'static': StaticViewSitemap,
    'page': PageSitemap,
}
