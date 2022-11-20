from rest_framework.generics import ListAPIView
from django.db.models import Avg, Count

from .serializers import PostListSerializer
from .models import Score, Post 


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        queryset = Post.objects.prefetch_related('postscore')\
            .annotate(score=Avg('postscore__score_number'), usernumber=Count('postscore__score_number'))\
                .values('score', 'title', 'usernumber')
        return queryset
    
