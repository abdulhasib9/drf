from django.urls import path 
from . import views

app_name = 'cbvapp'

urlpatterns = [
    path('cars/',views.Cars_list.as_view(),name='cars'),
    path('car_detail/<int:pk>/',views.Cars_detail.as_view(),name ='car_detail'),
   
]
