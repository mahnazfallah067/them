# Generated by Django 3.2.5 on 2021-09-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_category', '0003_remove_category_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='_shop_category_category_sub_category_+', to='shop_category.Category'),
        ),
    ]
