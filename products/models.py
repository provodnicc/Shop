from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
        return self.title
