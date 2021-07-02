from django import forms

class sendForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()