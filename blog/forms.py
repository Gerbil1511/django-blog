from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    This class is used to create a form for comments.
    """
    class Meta:
        """
        This class is used to define the fields of the form.
        """
        model = Comment
        fields = ('body',)