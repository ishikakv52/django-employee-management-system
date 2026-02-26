from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=220)
    eid=models.IntegerField()
    email=models.CharField(max_length=220)
    salary=models.CharField(max_length=220)
