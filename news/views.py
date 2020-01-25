from django.shortcuts import render, get_object_or_404
from django.views import View
from news.models import News


class NewsView(View):
    @staticmethod
    def get(request):
        news = News.objects.filter(is_active=True)

        context = {
            'news': news,
        }
        return render(request, 'news/news.html', context)


class NewsDetailView(View):
    @staticmethod
    def get(request, news_slug):
        news_item = get_object_or_404(News, slug=news_slug)

        context = {
            'news_item': news_item,
        }
        return render(request, 'news/news_detail.html', context)

