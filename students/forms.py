from django import forms
from .models import Student
import re

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name should contain only letters")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_regex, email):
            raise forms.ValidationError("Enter a valid email address.")
        
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) not in [10, 11, 12]:
            raise forms.ValidationError("Enter a valid phone number (10-12 digits).")
        return phone
