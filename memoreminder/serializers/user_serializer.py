from django.contrib.auth import password_validation
from rest_framework import serializers

from memoreminder.models import MemoUser, PostLike, CommentLike, Post, Comment
from memoreminder.serializers import DynamicFieldModelSerializer


class MemoUserSerializer(DynamicFieldModelSerializer):
    likes_received_count = serializers.SerializerMethodField(read_only=True)
    posts_count = serializers.SerializerMethodField(read_only=True)
    comments_received_count = serializers.SerializerMethodField(read_only=True)

    def get_likes_received_count(self, obj: MemoUser):
        return PostLike.objects.filter(post__creator_user=obj).count() + CommentLike.objects.filter(
            comment__memo_user=obj).count()

    def get_posts_count(self, obj: MemoUser):
        return Post.objects.filter(creator_user=obj).count()

    def get_comments_received_count(self, obj: MemoUser):
        return Comment.objects.filter(post__creator_user=obj).count()

    class Meta:
        model = MemoUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birthday_date',
            'likes_received_count',
            'posts_count',
            'comments_received_count',
            'friends',
            'created',
            'token',
        )

        read_only_fields = ('token', 'id', 'created')

    @staticmethod
    def validate_password(password):
        password_validation.validate_password(password)
        return password


class ListMemoUserSerializer(serializers.ModelSerializer):
    likes_received_count = serializers.SerializerMethodField(read_only=True)
    posts_count = serializers.SerializerMethodField(read_only=True)
    comments_received_count = serializers.SerializerMethodField(read_only=True)

    def get_likes_received_count(self, obj: MemoUser):
        return PostLike.objects.filter(post__creator_user=obj).count() + CommentLike.objects.filter(
            comment__memo_user=obj).count()

    def get_posts_count(self, obj: MemoUser):
        return Post.objects.filter(creator_user=obj).count()

    def get_comments_received_count(self, obj: MemoUser):
        return Comment.objects.filter(post__creator_user=obj).count()
    
    def update(self, instance, validated_data):
        raise serializers.ValidationError('قادر به ویرایش کاربران به صورت گروهی نیستید.')

    class Meta:
        model = MemoUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'friends',
            'phone_number',
            'likes_received_count',
            'posts_count',
            'comments_received_count',
        )

        read_only_fields = ('token', 'id', 'created')
