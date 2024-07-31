from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm as DjangoPasswordChangeForm, PasswordChangeForm
from .models import Ride, CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['leaving_from', 'going_to', 'date_of_departure', 'num_passengers']
        widgets = {
            'date_of_departure': forms.DateInput(attrs={'type': 'date'}),
            'num_passengers': forms.NumberInput(attrs={'min': 1, 'value': 1}),
        }
        error_messages = {
            'origin': {
                'required': 'Please enter the origin.',
            },
            'destination': {
                'required': 'Please enter the destination.',
            },
            'date': {
                'invalid': 'Enter a valid date.',
            }
        }
        

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

class CustomPasswordChangeForm(DjangoPasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Current Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm New Password')

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Current password is incorrect.')
        return old_password