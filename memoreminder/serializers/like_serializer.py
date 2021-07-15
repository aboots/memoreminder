from rest_framework import serializers

from memoreminder.models import PostLike
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class PostLikeSerializer(BaseTokenSerializer):
    memo_user_field_name = 'memo_user'

    class Meta:
        model = PostLike
        fields = (
            'id',
            'post',
            'memo_user',
            'created',
        )

        read_only_fields = ('id', 'created')


class MinimalPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('id', 'memo_user',)
        read_only_fields = ('id',)
