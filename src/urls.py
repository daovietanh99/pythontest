from django.urls import path, include
from rest_framework import routers
import src.views as views

router = routers.DefaultRouter()

router.register(r'question', views.QuestionView, basename='questions')
router.register(r'user', views.UserView, basename='users')
router.register(r'answer', views.AnswerView, basename='answers')

urlpatterns = [
    path('api/', include(router.urls)),
]