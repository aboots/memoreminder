from memoreminder.models import PostLike, CommentLike
from memoreminder.serializers import PostLikeSerializer
from memoreminder.serializers.like_serializer import CommentLikeSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class PostLikeModelViewSet(TokenModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    do_not_filter = True


class CommentLikeModelViewSet(TokenModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    do_not_filter = True
