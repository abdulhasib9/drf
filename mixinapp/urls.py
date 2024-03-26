from django.urls import path 
from . import views 

app_name = 'mixinapp'

urlpatterns = [
    #path('tests/',views.TestList.as_view()),
    path('tests/',views.TestListCreateAPIView.as_view())
]
