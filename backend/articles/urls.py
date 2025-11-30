from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet

from articles.views import ArticleDetailView, ArticleListView


articles_api_router = DefaultRouter()
articles_api_router.register(r'articles', ArticleViewSet, basename='article')


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),

]