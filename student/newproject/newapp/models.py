from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100,null=True)
    regno=models.IntegerField(default=0)
    year=models.IntegerField(default=0)
    dept=models.CharField(max_length=100,null=True)
    marks=models.IntegerField(default=0)
    

    def __str__(self): 
        return self.name


