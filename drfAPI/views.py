from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def list_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serilizers = StudentSerializer(students,many=True)
        return Response(serilizers.data,status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serialzer = StudentSerilizers(data = request.data)
        if serilizer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status = status.HTTP_201_CREATED)
        
        return Response(serialzer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data = request.data)
        if serilizer.is_valid():
            serializer.save()
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        