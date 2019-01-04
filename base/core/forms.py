from django import forms
from .models import Human, Talks

class TalksForm(forms.ModelForm):

   class Meta:
     model = Talks
     fields = ('human', 'topic', 'name', 'link')
