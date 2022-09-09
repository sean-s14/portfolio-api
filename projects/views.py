from django.shortcuts import render


# Rest Framework
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# Custom
from .serializers import ProjectSerializer
from .models import Project


class ProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = ()
    authentication_classes = ()


class ProjectDetail(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = ()
    authentication_classes = ()