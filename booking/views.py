from django.shortcuts import render
import random
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from booking.models import Ticket
from booking.serializers import TicketSerializer
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
        ticket =  Ticket.objects.create(**data)
        ticket_serialized = TicketSerializer(ticket)
        return Response(ticket_serialized.data, status=status.HTTP_201_CREATED)