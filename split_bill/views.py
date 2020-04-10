from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views import generic
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


def bill_details(request, bill_id):
    bill = get_object_or_404(Bill,
                             id=bill_id)
    return render(request,
                  'split_bill/detail.html',
                  {'bill': bill})

# class BillDetailView(generic.DetailView):
#     model = Bill
