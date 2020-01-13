from django.urls import path
from .views import HomePage

app_name = 'cms'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    # path('<slug:slug>/', PageDetail.as_view(), name='page')
]
