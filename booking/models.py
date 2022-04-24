from django.db import models
from users.models import User
import random
from trains.models import Trains, Route, Train_Status, Station, RouteStation 
from users.models import User

# Create your models here.



class Ticket(models.Model):
    pnr = models.IntegerField(primary_key=True, default=96311)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reg_user")
    book_date = models.DateTimeField(auto_now_add=True)
    train_class = models.CharField(max_length=10)
    ticket_no = models.IntegerField(default=5324)
    seat_no = models.IntegerField(default=0)
    date_of_journey = models.DateField()
    train =models.ForeignKey(Trains ,on_delete=models.CASCADE)
    route =models.ForeignKey(Route ,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        
        self.seat_no = self.seat_no + random.randint(0, 1000)
        self.ticket_no = self.ticket_no + random.randint(0, 100000)
        self.pnr = self.pnr + random.randint(0, 100000) #to generate random ticket number each time
        super().save(*args, **kwargs)
        
