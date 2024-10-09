

from django import forms
from .models import bk,Author
class Authorform(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name']


        widgets={
             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the author name'})
        }
class Bookform(forms.ModelForm):
    class Meta:
        model=bk
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the book name'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'enter the author name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter the price'})
        }
