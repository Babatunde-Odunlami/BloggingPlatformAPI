from django import forms
from .models import Username

#create a user creation form
class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) # helps not to display the password as strings
    confirm_password = forms.CharField(widget=forms.PasswordInput) # recapture password

    class Meta:
        model = Username
        fields = ('username', 'email', 'password', 'confirm_password')