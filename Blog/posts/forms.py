from django import forms
from .models import *

class BookDetails_Form(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'front_page_summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'detailed_summary':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'book_picture':forms.FileInput(attrs={'class':'form-control'}),
            'contributor':forms.TextInput(attrs={'class':'form-control'}),
        }
