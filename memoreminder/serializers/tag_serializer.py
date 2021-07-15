from rest_framework import serializers

from memoreminder.models import Tag
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class TagSerializer(BaseTokenSerializer):
    memo_user_field_name = 'creator_user'

    class Meta:
        model = Tag
        fields = (
            'id',
            'creator_user',
            'name',
            'color',
            'created',
        )

        read_only_fields = ('id', 'created')


class MinimalTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color',)
        read_only_fields = ('id',)
