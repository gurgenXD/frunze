from django.urls import path
from products.views import *


urlpatterns = [
    path('', CatalogueView.as_view(), name='catalogue'),
    path('change/bar_type/', ChangeBarTypeView.as_view(), name='change_bar_type'),
    path('search/result/', SearchResultView.as_view(), name='search_result'),
    path('products.json/', ProductsJsonView.as_view(), name='products_json'),
    path('<category_slug>/', CatalogueCategoryView.as_view(), name='catalogue_category'),
    path('<category_slug>/<subcategory_slug>/', CatalogueSubCategoryView.as_view(), name='catalogue_subcategory'),
    path('<category_slug>/<subcategory_slug>/<product_slug>/', CatalogueItemView.as_view(), name='catalogue_item'),
]
