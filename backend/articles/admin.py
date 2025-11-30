from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'content_preview', 
        'category', 
        'is_premium',
        'created_at',    
    )
    list_filter = ('category', 'created_at')
    search_fields = ('title',)

    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Article'