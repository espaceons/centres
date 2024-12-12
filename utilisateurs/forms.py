from django import forms
from django.contrib.auth.forms import UserCreationForm

from utilisateurs.models import CustomUser



class LoginViewForm(forms.Form):
    username = forms.CharField(max_length=255, label="nom d'utilisateur")
    password = forms.CharField(max_length=255, widget=forms.PasswordInput, label='Password')
    
    
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        
        fields = ['first_name','last_name','email','password1','password2']