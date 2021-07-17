from rest_framework import serializers

from memoreminder.models import PostFile
from memoreminder.serializers import BaseTokenSerializer


class PostFileSerializer(BaseTokenSerializer):
    memo_user_field_name = 'post__creator_user'

    def validate_post(self, post):
        if post.creator_user.pk != self.context['user']:
            raise serializers.ValidationError("this post doesn't belong to this user")
        return post

    def to_internal_value(self, data):
        if hasattr(data, '_mutable') and not getattr(data, '_mutable'):
            setattr(data, '_mutable', True)
        if 'post' in self.context:
            data['post'] = self.context['post']
        return super(PostFileSerializer, self).to_internal_value(data)


    class Meta:
        model = PostFile
        fields = (
            'id',
            'post',
            'file',
            'created',
        )

        read_only_fields = ('id', 'created')
