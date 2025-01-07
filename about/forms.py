from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    This class is used to create a form for collaboration requests.
    """
    class Meta:
        """
        This class is used to define the fields of the form.
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
        