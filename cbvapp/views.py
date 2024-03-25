from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from .models import Cars
from .serializers import CarSerializer
# from rest_framework.decorators import api_view 
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class Cars_list(APIView):
    def get(self,request):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid(self):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class Cars_detail(APIView):
    def get_object(request,pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    def put(self,request,pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
        