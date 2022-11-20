from django.urls import path, include

from blog.views import PostListAPIView, ScoreCreateAPIView

urlpatterns = [
    path('post/', PostListAPIView.as_view()),
    path('post/<int:id>/score/', ScoreCreateAPIView.as_view()),
]