from django.db import models


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

    def __str__(self):
        return self.title
