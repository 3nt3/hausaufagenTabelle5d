from django import forms
from django.utils.timezone import now

class AddForm(forms.Form):
    subject = forms.CharField(label='Fach')
    exercise = forms.CharField(label='Aufgabe', widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}))
    info = forms.CharField(label='Infos', widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}), required=False)
    date_created_at = forms.DateField(label='Von', initial=now())
    date_until = forms.DateTimeField(label='Bis')
    author = forms.CharField(label='Autor')

class EditForm(forms.Form):
    subject = forms.CharField(label='Fach')
    exercise = forms.CharField(label='Aufgabe', widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}))
    information = forms.CharField(label='Infos', widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}), required=False)
    date_until = forms.DateTimeField(label='Bis')
    #author = forms.CharField(label='Autor (Initialen)', max_length=2)