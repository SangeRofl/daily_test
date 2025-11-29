from django.contrib import admin

from quiz.models import Category, Question, Answer
from quiz.inlines import AnswerInline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


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


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    '''read only mode'''
    list_display = ('question_preview', 'description', 'is_correct')
    list_filter = ('is_correct', 'question__category')
    search_fields = ('description', 'question__description')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def question_preview(self, obj):
        return obj.question.description[:50] + '...'
    question_preview.short_description = 'Question'