from django.urls import path
from documents.views import *


urlpatterns = [
    path('', DocumentsView.as_view(), name='documents'),
]
