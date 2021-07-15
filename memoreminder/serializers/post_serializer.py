from django.conf import settings
from rest_framework import serializers

from memoreminder.models import Post, Tag
from memoreminder.serializers import MinimalPostLikeSerializer
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer
from memoreminder.serializers.comment_serializer import MinimalCommentSerializer
from memoreminder.serializers.tag_serializer import MinimalTagSerializer


class PostSerializer(BaseTokenSerializer):
    memo_user_field_name = 'creator_user'
    post_files = serializers.SerializerMethodField()
    likes = MinimalPostLikeSerializer(many=True, source='postlike_set', required=False)
    comments = MinimalCommentSerializer(many=True, source='comment_set', required=False)
    # tags = MinimalTagSerializer(many=True, required=False)

    def get_post_files(self, obj: Post):
        return [settings.DOMAIN + file_post.file.url for file_post in obj.postfile_set.all()]

    def validate_tags(self, tags):
        for tag in tags:
            if tag.creator_user.pk != self.context['user']:
                raise serializers.ValidationError('tag is not belong to this user')
        return tags

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        ls = []
        for tag in instance.tags.all():
            ls.append(MinimalTagSerializer(instance=tag).data)
        data['tags'] = ls
        return data

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
            'likes',
            'comments',
            'created',
            'modified',
        )

        read_only_fields = ('id', 'created', 'post_files', 'likes', 'comments')
