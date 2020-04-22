from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.views import generic
from django.forms import inlineformset_factory, modelformset_factory
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
    return render(request,
                  'split_bill/persons_list.html',
                  {'persons': persons,
                   'header': 'Persons list'})


def person_detail(request, person_id):
    person = get_object_or_404(Person,
                               id=person_id)
    if request.method == 'POST':
        p_bill_form = forms.PersonBillForm(request.POST)
        if p_bill_form.is_valid():
            p_bill = p_bill_form.save(commit=False)
            p_bill.person = person
            p_bill.save()
            return redirect('split_bill:person_detail',
                            person_id=person_id)

    else:
        p_bill_form = forms.PersonBillForm()
    return render(request,
                  'split_bill/person_detail.html',
                  {'person': person,
                   'p_bill_form': p_bill_form,
                   'header': 'Input {}`s part bill'.format(
                       person.person_name
                   )})


def final(request, bill_id):
    bill = get_object_or_404(Bill,
                             id=bill_id)
    persons = bill.person_set.all()
    for person in persons:
        summa = 0
        pbills = person.personbill_set.all()
        for pbill in pbills:
            summa += pbill.person_partbill
        person.summa = summa
        person.save()
    return render(request,
                  'split_bill/final.html',
                  {'bill': bill,
                   'header': 'Final result for bill {} \u263A'.format(
                       bill.full_bill
                   )})
