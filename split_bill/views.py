from django.shortcuts import get_object_or_404, render
from . import forms
from .models import Bill

# Create your views here.


def index(request):
    if request.method == 'POST':
        bill_form = forms.BillForm(request.POST)
        if bill_form.is_valid():
            bill = bill_form.save(commit=False)
            bill.split()
            bill.save()
            return render(request,
                          'split_bill/result.html',
                          {'bill': bill,
                           'header': 'Your`e result'})
    else:
        bill_form = forms.BillForm()
    return render(request,
                  'split_bill/index.html',
                  {'form': bill_form,
                   'header': 'Welcome to SplitBillApp!'})


def detail(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    return render(request, 'split_bill/detail.html', {'bill': bill})
