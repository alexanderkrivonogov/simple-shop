from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория товаров')
    parent = models.ForeignKey('self', related_name='children', verbose_name='Родитель', null=True, blank=True,
                               on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(verbose_name='Номер в списке')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['index']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    banner = models.ImageField(upload_to='banner', verbose_name='Баннер')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photo', blank=True)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return f'#{self.id} Фото'
