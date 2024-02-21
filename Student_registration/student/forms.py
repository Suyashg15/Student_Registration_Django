#For collecting data
from django import forms

class StudForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='Student Name')
    s_class=forms.CharField(max_length=30,label='Class')
    s_school=forms.CharField(max_length=30,label='School')
    s_addr=forms.CharField(max_length=30,label='Address')
    s_email=forms.EmailField(max_length=30,label='Email')
    

class SForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='Student Name')