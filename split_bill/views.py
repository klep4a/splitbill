from django.shortcuts import render
from . import forms

# Create your views here.


def index(request):
    if request.method == 'POST':
        bill_form = forms.BillForm(request.POST)
        if bill_form.is_valid():
            new_bill = bill_form.save(commit=False)
            new_bill.split()
            new_bill.save()
            return render(request,
                          'split_bill/detail.html',
                          {'bill': new_bill,
                           'header': 'Your`e result'})
    else:
        bill_form = forms.BillForm()
    return render(request,
                  'split_bill/index.html',
                  {'form': bill_form,
                   'header': 'Welcome to SplitBillApp!'})
