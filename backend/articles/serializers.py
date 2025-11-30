# serializers.py
from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    content_preview = serializers.CharField(read_only=True)
    full_content = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content_preview', 'full_content', 'is_premium', 'category', 'created_at']
    
    def get_full_content(self, obj: Article):
        request = self.context.get('request')
        user = request.user if request else None
        return obj.content_for_user(user)
    