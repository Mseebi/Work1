from rest_framework import viewsets
from . import models
from . import serializers
from .models import Movies

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view


#class MovieViewset(viewsets.ModelViewSet):
#    queryset = models.Movies.objects.all()
 #   serializer_class = serializers.MovieSerializer
def all_movs(request):
    movie = Movies.objects.all()
    if request.method == 'GET': 
        movie_serializer = serializers.MovieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    
    
def mov_d(request, name):
    
    movie_name = Movies.objects.filter(name=name)#.first()
    if request.method == 'GET': 
        movie_serializer = serializers.MovieSerializer()
        return JsonResponse(movie_serializer.data)