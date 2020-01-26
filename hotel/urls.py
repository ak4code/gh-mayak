from django.urls import path
from .views import PhotosListView, FeedbackListView

app_name = 'hotel'

urlpatterns = [
    path('photos/', PhotosListView.as_view(), name='photos'),
    path('feedback/', FeedbackListView.as_view(), name='feedback')
]
