from django.contrib.auth.models import User
from django.db import models
from shop_product.models import Product

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    text = models.TextField(max_length=400)


    def __str__(self):
        return f'{self.user}'


    # class Meta:
    #     fields = ('-date',)
    #



