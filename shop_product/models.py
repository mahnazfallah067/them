from django.db import models
from django.db.models import Q
from django.urls import reverse

from shop_category.models import Category
import os

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    ext = os.path.splitext(base_name)
    return ext


def upload_image_path(instance, filename):
    ext = get_filename_ext(filename)
    finalname = f"{instance.id} - {instance.title}{ext}"
    return f"products/{finalname}"


def upload_gallery_image_path(instance, filename):
    ext = get_filename_ext(filename)
    finalname = f"{instance.id} - {instance.title}{ext}"
    return f"products/galleries{finalname}"


class ProductManager(models.Manager):

    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)




class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='نام قالب')
    description = models.CharField(max_length=120, verbose_name='توضیحات' , blank=True)
    attribute = models.CharField(max_length=120, verbose_name='ویژگی' , blank=True)
    type = models.CharField(max_length=120, verbose_name='نوع قالب')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس')
    active = models.BooleanField(verbose_name='فعال/غیرفعال')
    owner = models.CharField(max_length=120, default=True)
    category = models.ManyToManyField(Category)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/product/{self.id}"

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصولات'