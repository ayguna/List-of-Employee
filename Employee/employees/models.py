from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=30)
    movie_description = models.CharField(max_length=150)


class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  