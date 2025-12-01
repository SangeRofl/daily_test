from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="tests"),
    path('quiz/<int:quiz_id>/', views.quiz, name="quiz"),
    path('rating/', views.rating, name="rating")
]