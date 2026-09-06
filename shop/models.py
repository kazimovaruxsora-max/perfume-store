from django.db import models


class Product(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', 'Мужской'
        FEMALE = 'female', 'Женский'
        UNISEX = 'unisex', 'Унисекс'

    class Category(models.TextChoices):
        EAU_DE_PARFUM = 'edp', 'Eau de Parfum'
        EAU_DE_TOILETTE = 'edt', 'Eau de Toilette'
        PARFUM = 'parfum', 'Parfum'
        EAU_DE_COLOGNE = 'edc', 'Eau de Cologne'
        NICHE = 'niche', 'Нишевая парфюмерия'
        OTHER = 'other', 'Другое'

    name = models.CharField('Название', max_length=200)
    brand = models.CharField('Бренд', max_length=120, blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена (сум)', max_digits=12, decimal_places=0)

    image = models.ImageField(
        'Фотография',
        upload_to='products/',
        blank=True,
        null=True,
        help_text='Загрузите фотографию через Admin. Если фото нет — на сайте будет показан placeholder.',
    )

    category = models.CharField(
        'Категория', max_length=20, choices=Category.choices,
        default=Category.OTHER, blank=True,
    )
    volume = models.CharField('Объём', max_length=30, blank=True, help_text='Например: 100 ml')
    gender = models.CharField(
        'Пол', max_length=10, choices=Gender.choices,
        default=Gender.UNISEX, blank=True,
    )

    top_notes = models.CharField('Верхние ноты', max_length=255, blank=True)
    middle_notes = models.CharField('Средние ноты', max_length=255, blank=True)
    base_notes = models.CharField('Базовые ноты', max_length=255, blank=True)

    in_stock = models.BooleanField('В наличии', default=True)
    is_new = models.BooleanField('Новинка', default=False)
    is_popular = models.BooleanField('Популярный', default=False)

    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Парфюм'
        verbose_name_plural = 'Парфюмы'
        ordering = ['-created_at']

    def __str__(self):
        if self.brand:
            return f'{self.brand} — {self.name}'
        return self.name

    def has_notes(self):
        return bool(self.top_notes or self.middle_notes or self.base_notes)
