from django import forms
from .models import BookersDetails

class BookerDetails_Form(forms.ModelForm):
    class Meta:
        model=BookersDetails
        fields='__all__'
        widgets={
            'booker_name':forms.TextInput(attrs={'class':'form-control'}),
            'booker_pic':forms.FileInput(attrs={'class':'form-control'}),
            'contribution':forms.TextInput(attrs={'class':'form-control'}),
            'about_me':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'contributed_books':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.TextInput(attrs={'class':'form-control'}),
        }
    