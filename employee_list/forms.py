from django import forms
from django.forms.utils import ValidationError
from .models import Candidate
from django import forms

class CandidateForm(forms.ModelForm):
    class Meta:
        model= Candidate
        fields=('name','contact','email','father_name','gender','highest_degree','address','aadhaar','work_experience')
        
