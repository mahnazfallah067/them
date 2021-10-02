from django.db import models

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=120, verbose_name='ایمیل')
    subject = models.CharField(max_length=120, verbose_name='عنوان پیام')
    text = models.TextField(max_length=1000, verbose_name='متن پیام')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده/ نشده')

    class Meta:
        verbose_name_plural = 'تماس با ما'
        verbose_name = 'تماس با ما'

    def __str__(self):
        return self.full_name
