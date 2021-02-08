from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    phone_number = models.IntegerField(max_length=13, default='')
    issue_message = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
