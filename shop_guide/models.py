from django.db import models

# Create your models here.


class Guide(models.Model):
    title = models.CharField(max_length=120, default=False, verbose_name='عنوان')
    guide1 = models.CharField(max_length=120, verbose_name='راهنمای 1')
    guide2 = models.CharField(max_length=120, verbose_name='راهنمای 2')
    guide3 = models.CharField(max_length=120, verbose_name='راهنمای 3')

    class Meta:
        verbose_name_plural = 'راهنمای سایت'
        verbose_name = 'راهنمای سایت'