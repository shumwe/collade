from django import forms
from tutorials.models import TutorialComments

class CommentForm(forms.ModelForm):
    class Meta:
        model = TutorialComments
        fields = ['parent','message']