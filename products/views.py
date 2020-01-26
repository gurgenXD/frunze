from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from products.models import SubCategory, Product, Category, BarType
from core.cart import Cart


class CatalogueView(View):
    @staticmethod
    def get(request):
        products = Product.objects.filter(is_active=True)

        context = {
            'products': products,
        }
        return render(request, 'products/catalogue.html', context)


class CatalogueItemView(View):
    @staticmethod
    def get(request, category_slug, subcategory_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)

        offer = product.offers.first()

        product_price = offer.price if offer else product.price
        in_stock = offer.in_stock if offer else product.in_stock

        category = get_object_or_404(Category, slug=category_slug)
        if subcategory_slug != 'all':
            subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        else:
            subcategory = None

        cart = Cart(request)
        in_cart = str(product.id) in cart.keys()

        context = {
            'product': product,
            'offer': offer,
            'product_price': product_price,
            'in_stock': in_stock,
            'in_cart': in_cart,
            'category': category,
            'subcategory': subcategory,
        }
        return render(request, 'products/catalogue-item.html', context)


class CatalogueCategoryView(View):
    @staticmethod
    def get(request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_active=True, category=category)

        context = {
            'category': category,
            'products': products,
        }
        return render(request, 'products/catalogue-category.html', context)

class CatalogueSubCategoryView(View):
    @staticmethod
    def get(request, category_slug, subcategory_slug):
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = SubCategory.objects.filter(category=category)

        products = Product.objects.filter(is_active=True, subcategory=subcategory)

        context = {
            'subcategory': subcategory,
            'subcategories': subcategories,
            'products': products,
            'category': category,
        }
        return render(request, 'products/catalogue-subcategory.html', context)


class ChangeBarTypeView(View):
    @staticmethod
    def get(request):
        offer_id = int(request.GET.get('offer_id'))
        offer = get_object_or_404(BarType, id=offer_id)

        context = {
            'product_price': '{:,}'.format(offer.price).replace(',', ' '),
            'in_stock': offer.in_stock,
        }
        return JsonResponse(context)


class SearchResultView(View):
    @staticmethod
    def get(request):
        query = request.GET.get('query', '')
        print(query)
        products = Product.objects.filter(title__icontains=query)
        
        context = {
            'products': products,
        }
        return render(request, 'products/search-result.html', context)


class ProductsJsonView(View):
    @staticmethod
    def get(request):
        query = request.GET.get('query', '')
        products = Product.objects.filter(title__icontains=query)
        search_list = [item.title for item in products]
        print(query)

        return JsonResponse(search_list, safe=False)

