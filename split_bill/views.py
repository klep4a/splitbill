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
            print(person_formset.cleaned_data)
            persons = person_formset.save(commit=False)
            print(request)
            for person in persons:
                person.save()
                print(person)
            return render(request,
                          'split_bill/persons_list.html',
                          {'bill': bill,
                           'persons_lists': persons,
                           'header': 'Input friends bills'})
    else:
        person_formset = PersonFormSet(instance=bill)
    return render(request,
                  'split_bill/bill_detail.html',
                  {'bill': bill,
                   'person_formset': person_formset,
                   'header': 'Bill detail'})


class PersonsListView(generic.ListView):
    model = Person
    # template_name = 'persons_list.html'
    # queryset = Person.objects.all()
    # context_object_name = 'persons_list'


class PersonDetailView(generic.DetailView):
    model = PersonBill
