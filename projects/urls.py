from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import (
    ProjectList,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)