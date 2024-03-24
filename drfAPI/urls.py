
from django.urls import path, re_path
from . import views

app_name = 'drfAPI'

urlpatterns = [
    path('students/',views.list_students, name='students'),
    #path('student/<int:pk>/',views.student_detail,'student_detail'),
]