from django import forms
from .models import *
from django.contrib.auth.models import User


class TeaForm(forms.ModelForm):

    class Meta:
        model = Tea
        fields = ('tea_name',)
