from django.shortcuts import render
from .models import Todo ,instagram
from  .serializer import Todoserialzier
from .serializer import instaserializer
from rest_framework import viewsets



class todoview(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=Todoserialzier

    
    

class instaview(viewsets.ModelViewSet):
    queryset=instagram.objects.all()
    serializer_class=instaserializer