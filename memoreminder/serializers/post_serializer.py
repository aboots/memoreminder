from django.conf import settings
from rest_framework import serializers

from memoreminder.models import Post
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class PostSerializer(BaseTokenSerializer):
    memo_user_field_name = 'creator_user'
    post_files = serializers.SerializerMethodField()

    def get_post_files(self, obj: Post):
        return [settings.DOMAIN + file_post.file.url for file_post in obj.postfile_set.all()]

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
            'post_files',
            'created',
            'modified',
        )

        read_only_fields = ('id', 'created', 'post_files')
