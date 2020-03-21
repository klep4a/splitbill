from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from .models import Bill
# import os
# Create your views here.


def index(request):
    context = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, 'split_bill/index.html', context)
