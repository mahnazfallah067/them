from django.urls import path
from .views import login_user, register_user, log_out

urlpatterns = [
    path('login', login_user),
    path('register', register_user),
    path('logout', log_out),

]