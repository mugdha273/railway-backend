from django.urls import path

from booking.views import TicketViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# router.register("book", TicketViewset, basename="api-ticket-booking")

urlpatterns = [
path("book/", TicketViewset.as_view(), name="booking"),
]

# urlpatterns += router.urls