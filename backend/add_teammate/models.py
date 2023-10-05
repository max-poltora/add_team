from django.db import models
from datetime import date

class Person(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    joined_date = models.DateField(null=True, default=date.today)
    
