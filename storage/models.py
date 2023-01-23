from django.db import models
from products.models import Product

PRODUCT_STATUSES = (
    ('In stock', 'In stock'),
    ('Pending', 'Pending'),
    ('Not available', 'Not available'),
)


class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=255, choices=PRODUCT_STATUSES)

    def __str__(self):
        return f'{self.product} - {self.quantity} items'

    @property
    def is_available(self):
        return self.quantity > 0



