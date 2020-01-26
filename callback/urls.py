from django.urls import path
from callback.views import *


urlpatterns = [
    path('add/', CallBackView.as_view(), name='callback'),
]
