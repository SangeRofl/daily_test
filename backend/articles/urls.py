from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet

from articles.views import ArticleDetailView, ArticleListView, ArticleDetailPartialView, ArticleListPartialView


articles_api_router = DefaultRouter()
articles_api_router.register(r'articles', ArticleViewSet, basename='article')


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('partial/', ArticleListPartialView.as_view(), name='article-list-partial'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/partial/', ArticleDetailPartialView.as_view(), name='article-detail-partial'),
]