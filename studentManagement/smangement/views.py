from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

