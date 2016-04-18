from django import forms
from .models import SignUp, User


class ContactForm(forms.Form):

    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def cleanEmail(self):
        return self.cleaned_data.get('email')

    def cleanFullName(self):
        return self.cleaned_data.get('full_name')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def cleanName(self):
        return self.cleaned_data.get('name')

    def cleanEmail(self):
        return self.cleaned_data.get('email')

    def cleanPassword(self):
        return self.cleaned_data.get('password')

