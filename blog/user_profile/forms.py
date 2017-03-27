from django import forms
from django.contrib.auth import get_user_model
from user_profile.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserRegistrForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'