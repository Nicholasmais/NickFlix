from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # def list(self, req):
    #     queryset = Movie.objects.all()
    #     serializer = MovieSerializer(queryset, many = True)
    #     return Response(serializer.data)