from memoreminder.models import PostLike
from memoreminder.serializers import PostLikeSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class PostLikeModelViewSet(TokenModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    do_not_filter = True

