from django.db import models


class Category(models.Model):
    name = models.CharField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models. CASCADE,
        related_name='questions',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField()

    class Meta:
        ordering = ['category', 'created_at']

    def __str__(self):
        return self.description[:60] + '...' if len(self.description) > 60 else self.description


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
    )
    description = models.CharField()
    is_correct = models.BooleanField(default=False)