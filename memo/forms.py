from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo # Connection of Form
        fields = ['title', 'description', 'content', 'image', 'video',]