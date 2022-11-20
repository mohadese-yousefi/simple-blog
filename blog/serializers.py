from rest_framework import serializers

from .models import Post, Score


class PostListSerializer(serializers.Serializer):
    score = serializers.DecimalField(min_value=0, max_digits=3, decimal_places=2)
    title =serializers.CharField() 
    usernumber = serializers.CharField() 


class ScoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score_number']