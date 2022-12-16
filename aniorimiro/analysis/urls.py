from django.urls import path
from . import views

urlpatterns = [
  path('map/', views.map, name='map'), 
  path('predict/', views.ListFunc, name='predict'),  
]