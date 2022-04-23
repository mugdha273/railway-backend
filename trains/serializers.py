from rest_framework import serializers

from trains.models import Route, RouteStation, Station, Train_Status, Trains


class TrainSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Trains
        fields = '__all__'
        
class RouteSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Route
        fields = '__all__'
        
class Train_StatusSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Train_Status
        fields = '__all__'
        
class StationSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Station
        fields = '__all__'
        
class RouteStationSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = RouteStation
        fields = '__all__'
        

