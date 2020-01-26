from core.models import TitleTag, Index
from products.models import Category
from core.cart import Cart


def context_info(request):
    seo_titles = TitleTag.objects.all()

    index_info = Index.objects.first()
    main_phone = index_info.phone if index_info else None

    categories = Category.objects.all()

    cart = Cart(request)

    context = {
        'seo_titles': seo_titles,
        'main_phone': main_phone,
        'categories': categories,
        'cart_len': len(cart),
    }

    return context