from django.shortcuts import render
from rest_framework import status
from rest_framework import generics,mixins
from .models import Test
#from rest_framework.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestSerializer
# Create your views here.

class TestList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
    def get(self,request):
        
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
class TestDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
    def get(self,requeest,pk):
        return self.retrive(requeest,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request):
        return self.destroy(request)