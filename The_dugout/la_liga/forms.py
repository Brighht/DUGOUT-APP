from django import forms 

class UserDetails(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.PasswordInput
    Gender = forms.CharField(max_length=10)