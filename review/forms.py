from django import forms
from .models import *
from django.contrib.auth.models import User


class TeaForm(forms.ModelForm):

    class Meta:
        model = Tea
        fields = ('tea_name',)

class ReviewForm(forms.ModelForm):
    tea = forms.ModelChoiceField(queryset=Tea.objects.all())
    class Meta:
        model = Review
        fields = ('review_text', 'username', 'tea')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site',)