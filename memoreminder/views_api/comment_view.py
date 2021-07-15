from memoreminder.models import Comment
from memoreminder.serializers import CommentSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class CommentModelViewSet(TokenModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    do_not_filter = True
