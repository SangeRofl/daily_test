# serializers.py
from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    content_preview = serializers.SerializerMethodField()
    full_content = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content_preview', 'full_content', 'is_premium', 'category', 'created_at']

    def get_content_preview(self, obj):
        return obj.content[:30] + '...' if len(obj.content) > 30 else obj.content

    def get_full_content(self, obj):
        # TODO: add check if user is premium
        return obj.content if not obj.is_premium else None