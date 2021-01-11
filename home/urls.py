from django.urls import path,include
from . import views

urlpatterns = [
    #home/main
    path('',views.index,name='index')
]