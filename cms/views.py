from django.views.generic import TemplateView, DetailView
from .models import Page


class HomePage(TemplateView):
    template_name = 'cms/home.html'


class PageDetail(DetailView):
    model = Page
    template_name = 'cms/page.html'