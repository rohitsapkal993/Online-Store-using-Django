from msilib.schema import Class
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=122, null=True, blank=True)
    last_name = models.CharField(max_length=122, null=True, blank=True)
    city = models.CharField(max_length=122, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return self.first_name
    
    

