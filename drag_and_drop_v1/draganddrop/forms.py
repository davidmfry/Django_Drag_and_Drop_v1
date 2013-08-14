from django import forms
from .models import UploadFormModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFormModel
        fields = ['name', 'email', 'phone', 'message']
    
