from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)  # сколько должно бфыь знаков, сколько знаков после запятой

    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='products')

    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        ordering = ['name']  # сортировка по названию по умолчанию

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])
    created_at = models.DateTimeField(auto_now_add=True)
