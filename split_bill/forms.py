from django import forms
from . import models


class BillForm(forms.ModelForm):
    class Meta:
        model = models.Bill
        exclude = ('date',)
