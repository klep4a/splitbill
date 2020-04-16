from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Bill(models.Model):
    full_bill = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField(default=timezone.now)
    split_num = models.PositiveSmallIntegerField(null=True)
    # objects = models.Manager()

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

    # class Meta:
    #     ordering = ['-date_time']

    # def get_absolute_url(self):
    #     return reverse('split_bill:bill_detail',
    #                    args=[self.id])


class Person(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    # person_count == Bill.split_num

    def __str__(self):
        return 'Name: {}'.format(self.person_name)


class PersonBill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    pers_bill = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'PBill: {} for {}'.format(self.pers_bill, self.person)
