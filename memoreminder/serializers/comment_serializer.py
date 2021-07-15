from rest_framework import serializers

from memoreminder.models import Comment
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer
from memoreminder.serializers.like_serializer import MinimalCommentLikeSerializer


class CommentSerializer(BaseTokenSerializer):
    memo_user_field_name = 'memo_user'
    likes = MinimalCommentLikeSerializer(many=True, source='commentlike_set')

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'post',
            'likes',
            'memo_user',
            'created',
        )

        read_only_fields = ('id', 'created', 'likes')


class MinimalCommentSerializer(serializers.ModelSerializer):
    likes = MinimalCommentLikeSerializer(many=True, source='commentlike_set')

    class Meta:
        model = Comment
        fields = ('id', 'memo_user', 'text', 'likes')
        read_only_fields = ('id', 'likes')
