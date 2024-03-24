from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Resopnse
# Create your views here.
def list_students(request):
    if request.method == 'GET':
        students = Student.models.all()
        serilizers = StudentSerializer(students,many=True)
        return Resopnse(serilizers,)
        