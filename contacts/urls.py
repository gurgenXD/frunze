from django.urls import path
from contacts.views import *


urlpatterns = [
    path('', ContactsView.as_view(), name='contacts'),
]
