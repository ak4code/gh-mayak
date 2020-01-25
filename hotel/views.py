from django.views.generic import ListView
from .models import Photo


class PhotosListView(ListView):
    model = Photo
    template_name = 'hotel/photo_list.html'
