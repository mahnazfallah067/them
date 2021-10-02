from django.shortcuts import render
from .models import Privacy

# Create your views her


def privacy(request):
    site_privacy = Privacy.objects.first()
    context = {
        'site_privacy': site_privacy

    }
    return render(request, 'privacy/roles.html', context)
