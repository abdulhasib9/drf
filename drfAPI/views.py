from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Resopnse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
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

def student_detail(request,pk):
    try:
        student = Student.objects.get(pk)
    except StudentNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Resopnse(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data = request.data)
        if serilizer.is_valid():
            serializer.save()
            return Resopnse(serializer.data)
        return Resopnse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Resopnse(status = status.HTTP_204_NO_CONTENT)
        