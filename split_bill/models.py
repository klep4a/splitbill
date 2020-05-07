from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Bill(models.Model):
    full_bill = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField(default=timezone.now)
    split_num = models.PositiveSmallIntegerField(null=True)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'Bill: {}, split: {}'.format(self.full_bill, self.split_num)

    def split(self):
        """Returns the list of splitted values."""
        self.split_list = []
        if self.split_num:
            for _ in range(self.split_num)[:-1]:
                self.split_list.append(round(self.full_bill / self.split_num, 2))
            self.split_list.append(self.full_bill - sum(self.split_list))
        else:
            self.split_list.append(self.full_bill)
        return self.split_list


class Person(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    # person_num == Bill.split_num
    summa = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # summa calculate when views.final called

    def __str__(self):
        return 'Name: {} for {}'.format(self.person_name, self.bill)


class PersonBill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person_partbill = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'PBill: {} for {}'.format(self.person_partbill, self.person)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{username} profile.".format(username=self.user.username)
