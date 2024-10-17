from django.db import models

# Create your models here.
class pgs(models.Model):
    pgname = models.CharField(max_length=100,primary_key=True)
    area = models.CharField(max_length=100)
    cost = models.IntegerField()
    def __str__(self):
        return self.area
class futurs(models.Model):
    pgname = models.ForeignKey(pgs,max_length=100,on_delete=models.CASCADE)
    food = models.CharField(max_length=100)
    powerbacup = models.CharField(max_length=100)
    hotwater = models.CharField(max_length=100)
    wifi = models.IntegerField()
    

