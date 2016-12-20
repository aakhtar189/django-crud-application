from __future__ import unicode_literals
from datetime import datetime

from django import forms
from django.conf import settings
from django.forms import FileInput
from django_countries import countries
from django.contrib.auth.models import User
from students.models import Student


class EditStudentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'required': 'required'}))

    class Meta:
        model=Student
        exclude = ['user']
        widgets = {
            'avatar': FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control'})

class CreateStudentForm(forms.ModelForm):
    pass        
