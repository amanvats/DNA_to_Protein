from django import forms
from django.utils.translation import ugettext_lazy as _
from . models import dna


class dnaForm(forms.ModelForm):

    class Meta:
        model = dna
        fields = ('dna_seq',)
        labels = {
            'dna_seq': _(''),
        }