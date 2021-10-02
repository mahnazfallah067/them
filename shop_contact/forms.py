from django import forms
from django.core import validators


class ContactForm(forms.Form):

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کامل خود را وارد نمایید'}),
        label=' نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل  را وارد نمایید'}),
        label='ایمیل  ',
        validators=[
            validators.MaxLengthValidator(150, '  ایمیل شما نمیتواند بیشتر از 150 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان  را وارد نمایید'}),
        label='عنوان پیام ',
        validators=[
            validators.MaxLengthValidator(150, 'عنوان شما نمیتواند بیشتر از 150 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا پیام  را وارد نمایید'}),
        label='متن پیام '
    )
