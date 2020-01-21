from django.urls import path
from core.views import *


urlpatterns = [
    path('load/subcategory/', SubCategoryLoadView.as_view(), name='load_subcategory'),
    path('', IndexView.as_view(), name='index'),
]
