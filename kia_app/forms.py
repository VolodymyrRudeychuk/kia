from django import forms
from .models import Token, Message
from django.contrib.auth import login
from django.contrib.auth.models import User


def schools():
    sls = User.objects.filter(is_staff=False)
    return [(school.id, school.first_name) for school in sls]


class LoginOrRequest(forms.Form):
    schools = forms.ChoiceField(choices=schools, label="Choos school")
    password = forms.CharField(required=False)
    email = forms.EmailField(max_length=255, required=False)

    def __init__(self, *args, **kwargs):
        super(LoginOrRequest, self).__init__(*args, **kwargs)
        self.fields['schools'].widget.attrs['class'] = 'form-control input-md'
        self.fields['password'].widget.attrs['class'] = 'form-control input-md'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['email'].widget.attrs['class'] = 'form-control input-md'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'

    def clean(self):
        if not self.cleaned_data['password'] and not self.cleaned_data['email']:
            raise forms.ValidationError('Enter password or enter email to request access')

        if self.cleaned_data['schools'] and not self.cleaned_data['password']:
            if not self.cleaned_data['email']:
                raise forms.ValidationError('Enter password or enter email to request access')

        if not self.cleaned_data['email']:
            if not self.school.check_password(self.cleaned_data['password']) and self.cleaned_data['schools']:
                raise forms.ValidationError('Password is not correct')

    def clean_schools(self):
        if not int(self.cleaned_data['schools']):
            raise forms.ValidationError('Choos School')
        self.school = User.objects.get(id=self.cleaned_data['schools'])
        return self.cleaned_data['schools']

    def login_user(self, request):
        self.school = User.objects.get(id=self.cleaned_data['schools'])
        self.school.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, self.school)

    def send_message(self):
        Message.objects.create(email=self.cleaned_data['email'], school=self.school)


