from .models import Todo,instagram
from rest_framework import serializers





class Todoserialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"




class instaserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=instagram
        fields="__all__"