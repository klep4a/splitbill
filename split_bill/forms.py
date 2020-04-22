from django import forms
from . import models


class BillForm(forms.ModelForm):
    class Meta:
        model = models.Bill
        exclude = ('date_time',)


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        exclude = ('bill', 'summa')


class PersonBillForm(forms.ModelForm):
    class Meta:
        model = models.PersonBill
        fields = ('person_partbill',)
