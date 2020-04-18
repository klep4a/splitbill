from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.views import generic
from django.forms import inlineformset_factory
from . import forms
from .models import Bill, Person, PersonBill

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


def bill_detail(request, bill_id):
    bill = get_object_or_404(Bill,
                             id=bill_id)
    PersonFormSet = inlineformset_factory(Bill,
                                          Person,
                                          form=forms.PersonForm,
                                          extra=bill.split_num,
                                          can_delete=False)
    if request.method == 'POST':
        person_formset = PersonFormSet(request.POST, instance=bill)
        if person_formset.is_valid():
            persons = person_formset.save(commit=False)
            for person in persons:
                person.save()
            return render(request,
                          'split_bill/persons_list.html',
                          {'persons': persons,
                              # 'bill': bill,
                           'header': 'Input friends bills'})
    else:
        person_formset = PersonFormSet(instance=bill)
    return render(request,
                  'split_bill/bill_detail.html',
                  {'bill': bill,
                   'person_formset': person_formset,
                   'header': 'Bill detail'})


def persons_list(request, bill_id):
    bill = get_object_or_404(Bill,
                             id=bill_id)
    persons = bill.person_set.all()
    print(bill.id, persons)
    return render(request,
                  'split_bill/persons_list.html',
                  {'persons': persons,
                   'header': 'Persons list'})


def person_detail(request, person_id):
    person = get_object_or_404(Person,
                               id=person_id)
    print(person.bill.pk, person.id, person)
    return render(request,
                  'split_bill/person_detail.html',
                  {'person': person,
                   'header': 'Person detail'})
