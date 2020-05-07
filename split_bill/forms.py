from django import forms
from django.contrib.auth.models import User

from . import models


class BillForm(forms.ModelForm):
    class Meta:
        model = models.Bill
        exclude = ('date_time', 'user')


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        exclude = ('bill', 'summa')


class PersonBillForm(forms.ModelForm):
    class Meta:
        model = models.PersonBill
        fields = ('person_partbill',)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Pass',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('bad password')
        return cd['password']
