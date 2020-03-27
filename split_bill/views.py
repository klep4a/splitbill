from django.shortcuts import render
# from django.urls.base import reverse
# from django.http.response import HttpResponseRedirect
# from django.template import loader
# from . import models
from . import forms
# from django.views import generic
# import os
# Create your views here.


def index(request):
    if request.method == 'POST':
        bill_form = forms.BillForm(request.POST)
        print(bill_form)
        if bill_form.is_valid():
            new_bill = bill_form.save(commit=False)
            print(request.POST)
            new_bill.split()
            new_bill.save()
            print(new_bill)
            return render(request,
                          'split_bill/detail.html',
                          {'bill': new_bill})
    else:
        bill_form = forms.BillForm()
    return render(request,
                  'split_bill/index.html',
                  {'form': bill_form})


# class DetailView(generic.DetailView):
#     model = models.Bill
#     template_name = 'split_bill/detail.html'
