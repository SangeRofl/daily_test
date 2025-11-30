from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from articles.models import Article
from articles.serializers import ArticleSerializer
from django.views.generic import ListView, DetailView


# TODO: move to api/ submodule
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.select_related('category').order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'


class ArticleListPartialView(ArticleListView):
    template_name = 'articles/list_partial.html'


class ArticleDetailPartialView(ArticleDetailView):
    template_name = 'articles/detail_partial.html'