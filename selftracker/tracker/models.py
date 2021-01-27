from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CycleTracker(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    start_time= models.TimeField()
    time_taken=models.TimeField()
    distance= models.FloatField()
    max_speed=models.FloatField()
    average_speed=models.FloatField()
    calories=models.FloatField()
    
class ActionPlanner(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    title= models.CharField(max_length=100)
    description = models.TextField() 