from django import forms

class sendCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)