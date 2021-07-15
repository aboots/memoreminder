from memoreminder.models import Tag, Post
from memoreminder.serializers import TagSerializer
from memoreminder.serializers.post_serializer import PostSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class PostModelViewSet(TokenModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
