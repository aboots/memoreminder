from memoreminder.models import Tag, Post
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class PostSerializer(BaseTokenSerializer):
    memo_user_field_name = 'creator_user'

    class Meta:
        model = Post
        fields = (
            'id',
            'creator_user',
            'title',
            'text',
            'tagged_people',
            'tags',
        )

        read_only_fields = ('id', 'created')
