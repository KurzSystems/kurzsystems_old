from django import forms
from crispy_forms.helper import FormHelper

from .models import NotifyEmail

class NotifyEmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(NotifyEmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''

    class Meta:
        model = NotifyEmail
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get(email)
            
            return email 