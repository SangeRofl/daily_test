from django.db import models
from quiz.models import Category


class Article(models.Model):
    title = models.CharField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def content_preview(self):
        return self.content[:30] + '...' if len(self.content) > 30 else self.content

    def content_for_user(self, user=None):
        # TODO: add check if user is premium
        if self.is_premium:
            return self.content if user and user.is_superuser else None
        return self.content