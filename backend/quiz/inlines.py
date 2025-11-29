from django.core.exceptions import ValidationError
from django.contrib import admin
from django import forms

from quiz.models import Answer


class AnswerOptionInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        valid_forms = [
            form for form in self.forms
            if form.cleaned_data and not form.cleaned_data.get('DELETE')
        ]

        if len(valid_forms) != 5:
            raise ValidationError('Question must have 5 answers.')

        correct_count = sum(
            1 for form in valid_forms
            if form.cleaned_data.get('is_correct')
        )
        if correct_count != 1:
            raise ValidationError('Question must have one right answer.')


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = AnswerOptionInlineFormSet
    extra = 0
