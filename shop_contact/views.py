from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs
from shop_setting.models import Setting

# Create your views here.


def contact_us(request):
    contact_form = ContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)

        contact_form = ContactForm()

    setting = Setting.objects.first()

    context = {
        'contact_form': contact_form,
        'setting': setting
    }
    return render(request, 'contact/contact_us.html', context)


