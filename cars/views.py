
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView

from cars.models import CarModel
from cars.serializers import CarSerializer, CarListSerializer
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class CarListCreateView(GenericAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    def get(self, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class CarRetrieveUpdateDestroyView(GenericAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    def get(self, *args, **kwargs):
        car = self.get_object()
        serializer = self.get_serializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        car = self.get_object()
        serializer = self.get_serializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, *args, **kwargs):
        data = self.request.data
        car = self.get_object()
        serializer = self.get_serializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)