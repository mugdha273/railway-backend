from rest_framework import serializers
from users.models import User
from booking.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = '__all__'
        
class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','phone_number']