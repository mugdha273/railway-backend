from django.shortcuts import render
import random
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from booking.models import Ticket
from users.models import User
from booking.serializers import TicketSerializer, PassengerSerializer
from trains.models import Trains, Route, Train_Status, Station, RouteStation 
# Create your views here.

class TicketViewset(APIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data= request.data)
        if not serializer.is_valid():
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data
        a = request.user
        # print(account.id)
        data["account"] = a
        ticket =  Ticket.objects.create(**data)
        # ticket.save()
        ticket_serialized = TicketSerializer(ticket)
        return Response(ticket_serialized.data, status=status.HTTP_201_CREATED)
    
class PassengerViewset(APIView):
    serializer_class =  PassengerSerializer
    queryset = User.objects.all()
    http_method_names = ["get"]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        account = request.user
        data = dict()
        data["personal_details"] =  PassengerSerializer(account).data
        print(account)
        
        personal_ticket = Ticket.objects.filter(account=account)
        print(type(personal_ticket))
        personal_ticket_data = TicketSerializer(personal_ticket, many = True).data
        
        data["ticket_details"] = [*personal_ticket_data]
        
        return Response(
            data,
            status = status.HTTP_200_OK
        )