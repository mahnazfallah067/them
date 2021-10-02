from django.db import models

# Create your models here.


class Setting(models.Model):
    address = models.CharField(max_length=120, verbose_name='ادرس')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(verbose_name='شماره تماس ', max_length=120)
    fax = models.CharField(verbose_name='فکس', max_length=120)

    class Meta:
        verbose_name_plural = 'تنظیمات سایت'
        verbose_name = 'تنظیمات سایت'

