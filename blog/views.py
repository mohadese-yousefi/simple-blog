from rest_framework.generics import ListAPIView, CreateAPIView
from django.db.models import Avg, Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import PostListSerializer, ScoreCreateSerializer
from .models import Score, Post 


class PostListAPIView(ListAPIView):
    """List of all posts with their scores
    """
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Post.objects.prefetch_related('postscore')\
            .annotate(score=Avg('postscore__score_number'), usernumber=Count('postscore__score_number'))\
                .values('score', 'title', 'usernumber')
        return queryset


class ScoreCreateAPIView(CreateAPIView):
    """ Add the score to the post
    """
    serializer_class = ScoreCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs['id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            score = Score.objects.get(post_id=post_id, user_id=request.user.id)
            score.score_number = serializer.data['score_number']
            score.save()
        except Score.DoesNotExist:
            serializer.validated_data['post_id'] = post_id
            serializer.validated_data['user_id'] = request.user.id
            serializer.save()
        
        return Response(serializer.data)