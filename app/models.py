from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.TextField()
    phone = models.IntegerField()
    myid = models.AutoField(primary_key=True)
    
    
    def __str__(self):
        return self.name