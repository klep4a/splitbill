from django.db import models
from django.utils import timezone

# Create your models here.


class Bill(models.Model):
    full_bill = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    split_num = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return str(self.full_bill) + str(self.split_num)

    def split(self):
        "Returns the list of splitted values."
        if self.split_num:
            self.split_list = []
            for _ in range(self.split_num)[:-1]:
                self.split_list.append(round(self.full_bill / self.split_num, 2))
            self.split_list.append(self.full_bill - sum(self.split_list))
        return self.split_list
