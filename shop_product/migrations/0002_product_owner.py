# Generated by Django 3.2.5 on 2021-09-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.CharField(default=True, max_length=120),
        ),
    ]
