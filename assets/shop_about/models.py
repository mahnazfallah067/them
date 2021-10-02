from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    text = models.TextField(max_length=10000, verbose_name=' متن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'درباره ما'
        verbose_name = 'درباره ما'