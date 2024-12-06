from django import forms


class LoginViewForm(forms.Form):
    username = forms.CharField(max_length=255, label="nom d'utilisateur")
    password = forms.CharField(max_length=255, widget=forms.PasswordInput, label='Password')