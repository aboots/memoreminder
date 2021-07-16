from rest_framework import serializers

from memoreminder.models import PostLike, CommentLike
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
    def to_representation(self, instance):
        data = super(MinimalPostLikeSerializer, self).to_representation(instance)
        user = instance.memo_user
        data['memo_user'] = {'id': user.pk,
                             'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name
                             }
        return data

    class Meta:
        model = PostLike
        fields = ('id', 'memo_user',)
        read_only_fields = ('id',)


class CommentLikeSerializer(BaseTokenSerializer):
    memo_user_field_name = 'memo_user'

    class Meta:
        model = CommentLike
        fields = (
            'id',
            'comment',
            'memo_user',
            'created',
        )

        read_only_fields = ('id', 'created')


class MinimalCommentLikeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(MinimalCommentLikeSerializer, self).to_representation(instance)
        user = instance.memo_user
        data['memo_user'] = {'id': user.pk,
                             'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name
                             }
        return data

    class Meta:
        model = CommentLike
        fields = ('id', 'memo_user',)
        read_only_fields = ('id',)
