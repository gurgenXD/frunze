from core.models import TitleTag, Index
from products.models import Category
from core.cart import Cart


def context_info(request):
    seo_titles = TitleTag.objects.all()
    main_phone = Index.objects.first().phone
    categories = Category.objects.all()

    cart = Cart(request)

    context = {
        'seo_titles': seo_titles,
        'main_phone': main_phone,
        'categories': categories,
        'cart_len': len(cart),
    }

    return context