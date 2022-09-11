from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import (
    ArticleList,
    ArticleDetail,
    ArticleDetailUpdate,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('<str:slug>/', ArticleDetail.as_view(), name='article_detail'),
    path('edit/<str:slug>/', ArticleDetailUpdate.as_view(), name='article_detail_update'),
    # path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)