from django import forms

class ProfileForm(forms.Form):
    """Profile forms"""
    
    first_name = forms.CharField(max_length = 50, required= False)
    last_name = forms.CharField(max_length = 50, required= False)
    phone_number = forms.CharField(max_length=20,required=False)
    
     