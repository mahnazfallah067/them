# Generated by Django 3.2.5 on 2021-09-07 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_category', '0002_auto_20210907_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
    ]
