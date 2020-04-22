from django.contrib import admin

# Register your models here.
from .models import Bill, Person, PersonBill

admin.site.register(Bill)
admin.site.register(Person)
admin.site.register(PersonBill)
