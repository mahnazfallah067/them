# Generated by Django 3.2.5 on 2021-09-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_product', '0004_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attribute',
            field=models.CharField(blank=True, max_length=120, verbose_name='ویژگی'),
        ),
    ]
