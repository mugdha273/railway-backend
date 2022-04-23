from django.contrib import admin
from .models import Trains, Route, Train_Status, Station, RouteStation
# Register your models here.

admin.site.register(Trains)
admin.site.register(Route)
admin.site.register(Train_Status)
admin.site.register(Station)
admin.site.register(RouteStation)