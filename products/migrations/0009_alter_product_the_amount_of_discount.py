# Generated by Django 5.0.6 on 2024-06-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_the_amount_of_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='the_amount_of_discount',
            field=models.PositiveIntegerField(verbose_name='The amount of discount'),
        ),
    ]
