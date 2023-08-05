from django import forms
from .models import Answer



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        
        # exclude = ('author','created_at' ) # all except author

        # fields = '__all__' # for all fields
        
        fields = ['answer', 'question']