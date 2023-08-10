from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemserializers

class MenuItemView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemserializers
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemserializers