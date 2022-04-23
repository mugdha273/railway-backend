from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from trains.serializers import TrainSerializer, RouteSerializer, Train_StatusSerializer, StationSerializer, RouteStationSerializer
from trains.models import Trains, Route, Train_Status, Station, RouteStation
from rest_framework import permissions
# Create your views here.

class TrainsViews(ModelViewSet):
    serializer_class = TrainSerializer
    queryset = Trains.objects.all()
    permission_classes = [permissions.AllowAny]

class RouteViews(ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
    permission_classes = [permissions.AllowAny]

class Train_StatusViews(ModelViewSet):
    serializer_class = Train_StatusSerializer
    queryset = Train_Status.objects.all()
    permission_classes = [permissions.AllowAny]

class StationViews(ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()
    permission_classes = [permissions.AllowAny]

class RouteStationViews(ModelViewSet):
    serializer_class = RouteStationSerializer
    queryset = RouteStation.objects.all()
    permission_classes = [permissions.AllowAny]



    
