from django.contrib import admin

from quiz.models import Category, Question, Answer
from quiz.inlines import AnswerInline


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('text_preview', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('description',)
    date_hierarchy = 'created_at'

    def text_preview(self, obj):
        # TODO: merge with Question.__str__ logic
        return obj.description[:60] + '...' if len(obj.description) > 60 else obj.description
    text_preview.short_description = 'Question'
