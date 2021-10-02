from django.shortcuts import render
from .models import AboutUs
from shop_setting.models import Setting

# Create your views here.


def about_us(request):
    about_site = AboutUs.objects.first()
    setting = Setting.objects.first()
    context = {
        'about_site': about_site,
        'setting': setting

    }
    return render(request, 'about/about_us.html', context)
