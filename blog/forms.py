from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # important to add the " , " so python can read it as a Tuple instead of a String. 
        fields = ('body',)