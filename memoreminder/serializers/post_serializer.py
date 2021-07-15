from rest_framework import serializers

from memoreminder.models import Tag, Post
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class PostSerializer(BaseTokenSerializer):
    memo_user_field_name = 'creator_user'

    def validate_tags(self, tags):
        for tag in tags:
            if tag.creator_user.pk != self.context['user']:
                raise serializers.ValidationError('tag is not belong to this user')
        return tags
        
    class Meta:
        model = Post
        fields = (
            'id',
            'creator_user',
            'title',
            'text',
            'tagged_people',
            'tags',
            'created',
            'modified',
        )

        read_only_fields = ('id', 'created')
