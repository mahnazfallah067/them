from django.urls import path
from .views import site_guide

urlpatterns = [
    path('site-guide', site_guide),


]