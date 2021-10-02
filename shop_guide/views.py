from django.shortcuts import render
from .models import Guide

# Create your views here.


def site_guide(request):

    guide = Guide.objects.first()
    context = {
        'guide': guide

    }
    return render(request, 'guide/guide.html', context)