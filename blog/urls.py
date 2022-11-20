from django.urls import path, include

from blog.views import PostListAPIView

urlpatterns = [
    path('post/', PostListAPIView.as_view())
]