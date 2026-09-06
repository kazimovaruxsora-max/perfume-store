from django.contrib import admin
from django.utils.html import format_html

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail', 'name', 'brand', 'price', 'category',
        'gender', 'in_stock', 'is_new', 'is_popular', 'created_at',
    )
    list_display_links = ('thumbnail', 'name')
    list_editable = ('in_stock',)
    list_filter = ('category', 'gender', 'in_stock', 'is_new', 'is_popular')
    search_fields = ('name', 'brand')
    ordering = ('-created_at',)
    list_per_page = 25

    fieldsets = (
        ('Основное', {
            'fields': ('name', 'brand', 'price', 'image')
        }),
        ('Характеристики', {
            'fields': ('category', 'volume', 'gender', 'in_stock', 'is_new', 'is_popular')
        }),
        ('Описание и ноты аромата', {
            'fields': ('description', 'top_notes', 'middle_notes', 'base_notes')
        }),
    )

    @admin.display(description='Фото')
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:48px;height:48px;object-fit:cover;'
                'border-radius:6px;" />',
                obj.image.url,
            )
        return format_html(
            '<div style="width:48px;height:48px;border-radius:6px;background:#f1ece3;'
            'display:flex;align-items:center;justify-content:center;font-size:9px;'
            'color:#a08e70;text-align:center;">нет фото</div>'
        )
