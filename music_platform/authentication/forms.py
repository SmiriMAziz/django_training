from django import forms


class SigninForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
