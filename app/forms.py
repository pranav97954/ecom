from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User 
from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput({'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput({'autofocus' : 'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput({'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput({'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput({'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput({'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput({'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','mobile','locality','city','state','zipcode']
        widgets={
            'name':forms.TextInput({'class':'form-control'}),
            'locality':forms.TextInput({'class':'form-control'}),
            'city':forms.TextInput({'class':'form-control'}),
            'mobile':forms.NumberInput({'class':'form-control'}),
            'state':forms.Select({'class':'form-control'}),
            'zipcode':forms.NumberInput({'class':'form-control'}),

        }