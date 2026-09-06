"""
Команда для наполнения каталога товарами.

Запуск:
    python manage.py seed_products

Ниже — ваш реальный список ароматов (27 позиций), названия и цены
использованы точно так, как вы их предоставили. Бренд оставлен пустым —
при желании можно вписать его вручную через /admin/.

Фото сюда не добавляется — оно загружается позже через /admin/.
Если товар с таким названием уже есть в базе — он не будет продублирован.
"""

from django.core.management.base import BaseCommand

from shop.models import Product

PRODUCTS = [
    {"name": "LM MOONTOBACCO", "price": 350000},
    {"name": "Genius Parfums MY WAY EDP", "price": 300000},
    {"name": "Fworld Hayaati.m.", "price": 300000},
    {"name": "LM Feramon Intrige", "price": 250000},
    {"name": "Fworld Blue Magician", "price": 300000},
    {"name": "Fworld Prive YYY EDP u", "price": 300000},
    {"name": "JB PURA EDP u", "price": 300000},
    {"name": "FWorld Esscentric 02", "price": 250000},
    {"name": "World Bavaria Lapurd", "price": 250000},
    {"name": "Fworld Exclusive Imperium", "price": 400000},
    {"name": "Fworld Intense Noir u", "price": 300000},
    {"name": "Emir A Chaos in The", "price": 300000},
    {"name": "La Fede Aura Crisp", "price": 250000},
    {"name": "MPF Maha w 100ml", "price": 300000},
    {"name": "JB Barrie ITALIYA", "price": 350000},
    {"name": "ARABIYAT AL Faris Arabe EDP u 100ml", "price": 250000},
    {"name": "La Fede intoicate", "price": 700000},
    {"name": "Luxury the Imperial", "price": 300000},
    {"name": "Gaba luxury", "price": 400000},
    {"name": "Gaba harmony", "price": 350000},
    {"name": "Atom", "price": 350000},
    {"name": "VOLARE ARCTIC BREEZE", "price": 350000},
    {"name": "VOLARE LUMINOUS WAVES", "price": 450000},
    {"name": "VOLARE ABOVE THE COLOUDS", "price": 400000},
    {"name": "VOLARE MOROCCAN DREAM", "price": 350000},
    {"name": "ROVENA NICHE EXTRACT", "price": 450000},
    {"name": "MAMLAKAT ALOUD ASHAAB", "price": 350000},
]


class Command(BaseCommand):
    help = 'Наполняет каталог товарами из списка PRODUCTS (ваш реальный список).'

    def handle(self, *args, **options):
        created_count = 0
        skipped_count = 0

        for item in PRODUCTS:
            _, created = Product.objects.get_or_create(
                name=item['name'],
                brand=item.get('brand', ''),
                defaults={
                    'price': item['price'],
                    'gender': item.get('gender', Product.Gender.UNISEX),
                    'category': item.get('category', Product.Category.OTHER),
                    'volume': item.get('volume', ''),
                },
            )
            if created:
                created_count += 1
            else:
                skipped_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Готово. Добавлено новых товаров: {created_count}. '
            f'Уже существовало (пропущено): {skipped_count}.'
        ))
