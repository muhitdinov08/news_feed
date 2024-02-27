from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=56)
    email = forms.EmailField()
    message = forms.CharField(max_length=150)

    def save(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]
        Contact.objects.create(name=name, email=email, message=message)
