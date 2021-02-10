from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Departments.models import userInformation

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")
    #organizations = forms.ModelChoiceField(queryset=organizations.objects.all(), initial=0)

    class Meta:
        model = userInformation
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "nationality",
            "national_id_number",
            "address",
            "organizations",
            "organizational_role",
            "reference_email",
            "describtion",
            "username",
            "email",
            "password1",
            "password2"        
        )

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = userInformation
        fields = ('email','password')
    
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Your Are Not a Valid User")