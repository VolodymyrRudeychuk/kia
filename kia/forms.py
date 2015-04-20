from django import forms
from .models import Token, Message
from django.contrib.auth import login


class TokenForm(forms.Form):
    token = forms.UUIDField(
        error_messages={
            'invalid': 'You token is not valid.'
        }
    )

    def __init__(self, *args, **kwargs):
        super(TokenForm, self).__init__(*args, **kwargs)
        self.fields['token'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['token'].widget.attrs['placeholder'] = 'Enter token'

    def clean_token(self):
        token = Token.objects.filter(token=self.cleaned_data['token'], active=True)
        if not token.exists():
            raise forms.ValidationError("You don't have access!")
        else:
            self.token = token[0]
        return self.cleaned_data['token']

    def login_user(self, request):
        self.token.user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, self.token.user)
        print 'privet', self.token.user


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'email', 'message', )