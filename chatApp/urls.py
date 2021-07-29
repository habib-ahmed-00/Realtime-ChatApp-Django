from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.home),
    path('<str:room>/' , views.room),
    path('checkview' , views.checkview),
]