from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from products.models import SubCategory, Product
from core.models import Index, Advantage
from news.models import News
from contacts.models import *
from callback.forms import CallBackForm


class SubCategoryLoadView(View):
    @staticmethod
    def get(request):
        category_id = request.GET.get('category_id')
        subcategories = SubCategory.objects.filter(category=category_id)

        context = {
            'subcategories': [(item.id, item.title) for item in subcategories],
        }
        return JsonResponse(context)


class IndexView(View):
    @staticmethod
    def get(request):
        index_info = Index.objects.first()
        advantages = Advantage.objects.filter(is_active=True)
        main_news = News.objects.filter(is_active=True).order_by('-created')[:3]

        main_products = Product.objects.filter(is_active=True).order_by('-created')[:4]

        addresses = Address.objects.all()
        phones = Phone.objects.all()
        faxes = Fax.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()

        callback_form = CallBackForm()

        context = {
            'index_info': index_info,
            'advantages': advantages,
            'main_news': main_news,
            'main_products': main_products,
            'addresses': addresses,
            'phones': phones,
            'faxes': faxes,
            'emails': emails,
            'map_code': map_code,
            'callback_form': callback_form,
        }
        return render(request, 'core/index.html', context)


class AboutView(View):
    @staticmethod
    def get(request):

        context = {
        }
        return render(request, 'core/about.html', context)
