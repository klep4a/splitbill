from django.db import models
from django.utils import timezone

# Create your models here.


class Bill(models.Model):
    full_bill = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    split_num = models.PositiveSmallIntegerField(null=True)


    def __str__(self):
        return ' '.join(map(str, self.__dict__.values()))

    def split(self):
        "Returns the list of splitted values."
        if self.split_num:
            self.s_v = []
            for _ in range(self.split_num)[:-1]:
                self.s_v.append(round(self.full_bill / self.split_num, 2))
            self.s_v.append(self.full_bill - sum(self.s_v))
        return self.s_v, sum(self.s_v)