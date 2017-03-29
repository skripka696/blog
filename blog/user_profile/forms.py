from django import forms
from django.contrib.auth import get_user_model
from user_profile.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from blog.settings import RECAPTCHA_PRIVATE_KEY
import requests
import json


class BootstrapStyleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BootstrapStyleForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserLoginForm(BootstrapStyleForm, AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


class UserRegistrForm(BootstrapStyleForm, UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = {
            'secret': RECAPTCHA_PRIVATE_KEY,
            'response': self.data.get('g-recaptcha-response'),
        }
        captch_check = requests.post(
            ' https://www.google.com/recaptcha/api/siteverify', data=data)
        result = json.loads(captch_check.text)
        if result['success']:
            self.cleaned_data['captcha'] = True
            return self.cleaned_data
        else:
            raise forms.ValidationError('invalid captcha')

