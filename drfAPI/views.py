from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Resopnse
from rest_framework import status

# Create your views here.
def list_students(request):
    if request.method == 'GET':
        students = Student.models.all()
        serilizers = StudentSerializer(students,many=True)
        return Resopnse(serilizers.data,status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serialzer = StudentSerilizers(data = request.data)
        if serilizer.is_valid():
            serialzer.save()
            return Resopnse(serialzer.data,status = status.HTTP_201_CREATED)
        
        return Response(serialzer.errors,status = status.HTTP_400_BAD_REQUEST)

        