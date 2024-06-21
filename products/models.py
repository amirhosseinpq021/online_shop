from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='cover/')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    discount = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField(null=True)
    sell_price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

    @property
    def discounted_price(self):
        return ((self.price) * (self.discount)) / 100

    @property
    def sell_price(self):
        return (self.price) - (self.discounted_price)
