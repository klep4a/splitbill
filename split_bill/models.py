from django.db import models

# Create your models here.


class Bill(models.Model):
    full_bill = models.DecimalField(max_digits=5, )
    date = models.DateTimeField(default=timezone.now)
