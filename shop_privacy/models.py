from django.db import models

# Create your models here.


class Privacy(models.Model):
    header = models.CharField(max_length=120, verbose_name='هدر')
    title = models.CharField(max_length=120, verbose_name='عنوان')
    description = models.TextField(max_length=1000, default=False, verbose_name='توضیحات')


    class Meta:
        verbose_name_plural = 'قوانین سایت'
        verbose_name = 'قوانین سایت'
