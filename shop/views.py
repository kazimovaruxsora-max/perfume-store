from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    popular = Product.objects.filter(is_popular=True)[:8]
    new_arrivals = Product.objects.filter(is_new=True)[:8]

    # Если ничего не помечено вручную — покажем последние добавленные,
    # чтобы главная страница не выглядела пустой.
    if not popular.exists():
        popular = Product.objects.all()[:8]
    if not new_arrivals.exists():
        new_arrivals = Product.objects.all().order_by('-created_at')[:8]

    categories = Product.Category.choices

    context = {
        'popular': popular,
        'new_arrivals': new_arrivals,
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)


def catalog(request):
    products = Product.objects.all()

    query = request.GET.get('q', '').strip()
    gender = request.GET.get('gender', '').strip()
    category = request.GET.get('category', '').strip()
    sort = request.GET.get('sort', '').strip()

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(brand__icontains=query)
        )

    if gender in dict(Product.Gender.choices):
        products = products.filter(gender=gender)

    if category in dict(Product.Category.choices):
        products = products.filter(category=category)

    sort_map = {
        'price_asc': 'price',
        'price_desc': '-price',
        'newest': '-created_at',
    }
    products = products.order_by(sort_map.get(sort, '-created_at'))

    context = {
        'products': products,
        'query': query,
        'gender': gender,
        'category': category,
        'sort': sort,
        'gender_choices': Product.Gender.choices,
        'category_choices': Product.Category.choices,
    }
    return render(request, 'shop/catalog.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})
