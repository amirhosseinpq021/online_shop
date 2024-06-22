from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse


class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


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

    objects = models.Manager()
    active_objects = ActiveProductManager()

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


class ActivCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActivCommentManager, self).get_queryset().filter(is_active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('خیلی بد بود', 'خیلی بد بود'),
        ('خوب بود', 'خوب بود'),
        ('خیلی عالی بود', 'خیلی عالی بود'),
    ]
    RECOMMEND = [
        ('اصلا پیشنهاد نمیکنم', 'اصلا پیشنهاد نمیکنم'),
        ('حتما پیشنهاد میکنم', 'حتما پیشنهاد میکنم'),
    ]
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    is_active = models.BooleanField(default=True)
    stars = models.CharField(max_length=100, choices=PRODUCT_STARS, blank=True)
    recommend = models.CharField(max_length=100, choices=RECOMMEND, blank=True)

    objects = models.Manager()
    active_comments_manager = ActivCommentManager()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])




