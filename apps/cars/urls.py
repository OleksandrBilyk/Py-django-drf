
from django.urls import path
from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_update_delete')
]
