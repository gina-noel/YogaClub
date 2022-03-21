from django import forms
from .models import Classes, ClassDetail, Pricing, Schedule

class ClassForm(forms.ModelForm):
    class Meta:
        model=Classes
        fields='__all__'

