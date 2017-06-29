from django import forms
from . models import dna

class dnaForm(forms.ModelForm):

    class Meta:
        model = dna
        fields = ('dna_seq',)
