from django import forms
from Pollapp.models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer','question']