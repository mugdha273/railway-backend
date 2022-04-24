from django.db import models

# Create your models here.


class Route(models.Model):
    rid=models.CharField(max_length=50)
    ostation = models.CharField(max_length=50)
    dstation = models.CharField(max_length=50)
    def __str__(self):
        return self.rid
    
class Trains(models.Model):
    train_name = models.CharField(max_length=50)
    train_type = models.CharField(max_length=50)
    train_number = models.CharField(max_length=10)
    rid=models.ForeignKey(Route,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.train_name

class Train_Status(models.Model):
    train_number =models.ForeignKey(Trains, on_delete=models.CASCADE)
    total_seats = models.IntegerField()
    booked_seats = models.IntegerField()
    total_fare = models.IntegerField()
    rid=models.ForeignKey(Route,on_delete=models.CASCADE)
    running_status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.train_number.train_name

class Station(models.Model):
    station_code=models.CharField(primary_key=True,max_length=50)
    station_name = models.CharField(max_length=50)
    station_type = models.CharField(max_length=10)
    def __str__(self):
        return self.station_code

class RouteStation(models.Model):
    train_number =models.ForeignKey(Trains,on_delete=models.CASCADE)
    station_code=models.ForeignKey(Station,on_delete=models.CASCADE)
    rid=models.ForeignKey(Route ,on_delete=models.CASCADE)
    departure_time=models.CharField(max_length=50)
    arrival_time=models.CharField(max_length=50)
    
    def __str__(self):
        return self.train_number.train_name
