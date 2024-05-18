
from django.urls import path
from cars.views import CarTestView

urlpatterns = [
    path('carsTest/', CarTestView.as_view())
]
