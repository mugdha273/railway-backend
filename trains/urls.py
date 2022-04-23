from django.urls import path

from trains import views
from trains.views import TrainsViews, RouteViews, StationViews,Train_StatusViews, RouteStationViews

urlpatterns = [
    path('trains/', TrainsViews.as_view({'get': 'list'}), name= 'trains'),
    path('route/', RouteViews.as_view({'get': 'list'}), name= 'routes'),
    path('train_status/', Train_StatusViews.as_view({'get': 'list'}), name= 'train_Status'),
    path('station/', StationViews.as_view({'get': 'list'}), name= 'station'),
    path('route-station/', RouteStationViews.as_view({'get': 'list'}), name= 'route-station'),
]
