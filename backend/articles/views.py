from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from articles.models import Article
from articles.serializers import ArticleSerializer

from django.views.generic import TemplateView


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.select_related('category').order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleListView(TemplateView):
    template_name = 'articles/list.html'

class ArticleDetailView(TemplateView):
    template_name = 'articles/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_id'] = kwargs['pk']
        return context