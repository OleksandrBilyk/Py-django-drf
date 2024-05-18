
from django.urls import path
from cars.views import CarTestView, CarDetailView, CarListCreateView

urlpatterns = [
    path('carsTest', CarTestView.as_view()),
    path('carDetail/<int:pk>', CarDetailView.as_view()),
    path('cars', CarListCreateView.as_view())
]
