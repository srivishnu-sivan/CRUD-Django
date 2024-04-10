from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from .serializers import CarsSerializers


class CarViewset(APIView):
    def get(self, request, id=None):
        
        car_name = request.query_params.get('car_name')
        car_model = request.query_params.get('car_model')
        car_version = request.query_params.get('car_version')
        car_price = request.query_params.get('car_price')
        
        
        if id:
            item = models.Cars.objects.get(id=id)
            serializer = CarsSerializers(item, many=True)
            return Response({"status" : "success", "data" : serializer.data}, status=status.HTTP_200_OK)
        if car_name : 
            items = models.Cars.objects.filter(car_name__icontains = car_name)
            serializer = CarsSerializers(items, many=True)
            return Response({"status" : "success", "data" : serializer.data}, status=status.HTTP_200_OK)
        if car_version :
            item = models.Cars.objects.filter(car_version__icontains = car_version)
            serializer = CarsSerializers(item, many=True)
            return Response({"status": "success", "data" : serializer.data}, status=status.HTTP_200_OK)
        if car_model :
            item = models.Cars.objects.filter(car_model__icontains = car_model)
            serializer = CarsSerializers(item, many=True)
            return Response({"status": "success", "data" : serializer.data}, status=status.HTTP_200_OK)
        if car_price :
            item = models.Cars.objects.filter(car_price__icontains = car_price)
            serializer = CarsSerializers(item, many=True)
            return Response({"status": "success", "data" : serializer.data}, status=status.HTTP_200_OK)
        
        else : 
            return Response({"status" : "failed"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self, request): # Get parameters from the requ
        
        serializer = CarsSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        