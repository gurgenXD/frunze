from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from products.models import SubCategory
from core.models import Index, Advantage


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

        context = {
            'index_info': index_info,
            'advantages': advantages,
        }
        return render(request, 'core/index.html', context)


class AboutView(View):
    @staticmethod
    def get(request):

        context = {
        }
        return render(request, 'core/about.html', context)


# class ExtendedFlatPageView(View):
#     @staticmethod
#     def get(request):

#         context = {
#         }
#         return render(request, 'flatpages/default.html', context)
