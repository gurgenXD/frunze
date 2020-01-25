from django.urls import path
from news.views import *


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<news_slug>/', NewsDetailView.as_view(), name='news_detail'),
]
