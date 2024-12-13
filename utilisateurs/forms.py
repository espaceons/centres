from django import forms
from django.contrib.auth.forms import UserCreationForm

from utilisateurs.models import CustomUser



class LoginViewForm(forms.Form):
    username = forms.CharField(max_length=255, label="nom d'utilisateur")
    password = forms.CharField(max_length=255, widget=forms.PasswordInput, label='Password')
    


class RegisterViewForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']