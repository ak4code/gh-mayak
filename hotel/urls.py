from django.urls import path
from .views import PhotosListView

urlpatterns = [
    path('photos/', PhotosListView.as_view(), name='photos')
]
