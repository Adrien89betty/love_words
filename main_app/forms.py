from django import forms
from .models import UserProfile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'partner_name',
            'partner_email',
            'partner_birthday',
            'partner_nickname',
            'partner_description'
        ]
        labels = {
            'partner_name': '',
            'partner_email': '',
            'partner_birthday': '',
            'partner_nickname': '',
            'partner_description': ''
        }
