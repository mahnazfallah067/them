from django import forms
from django.core import validators
from django.contrib.auth.models import User


class LoginForms(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام و نام خانوادگی خود  را وارد نمایید'}),
        label='ایمیل '
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا پسوورد خود را وارد نمایید'}),
        label='پسوورد'
    )


class RegisterForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری را وارد نمایید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(10, 'تعداد کاراکترهای وارد شده بیشتر از ده نمی تواند باشد'),
            validators.MinLengthValidator(2, 'تعداد کاراکترهای وارد شده کمتر از دو نمیتواند باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا پسوورد خود را وارد نمایید'}),
        label='پسوورد'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا پسوورد خود را دوباره وارد نمایید'}),
        label='پسوورد'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_username = User.objects.filter(username=username).exists()

        if is_exists_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_email = User.objects.filter(email=email).exists()

        if is_exists_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری است')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('پسووردها مغایرت دارند')
        return password








