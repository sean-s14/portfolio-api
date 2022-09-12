from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import (
    ProjectList,
    ProjectDetail,
    ProjectDetailUpdate,
    ProjectDetailDelete,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list'),
    path('<str:slug>/', ProjectDetail.as_view(), name='project_detail'),
    path('edit/<str:slug>/', ProjectDetailUpdate.as_view(), name='project_detail_update'),
    path('delete/<str:slug>/', ProjectDetailDelete.as_view(), name='project_detail_delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)