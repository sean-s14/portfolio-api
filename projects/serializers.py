from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ("id", "title", "slug", "category", "imageURI", "link", "description", "date_created")
