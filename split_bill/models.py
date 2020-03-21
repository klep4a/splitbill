from django.db import models
from django.utils import timezone

# Create your models here.


class Bill(models.Model):
    full_bill = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.full_bill)
