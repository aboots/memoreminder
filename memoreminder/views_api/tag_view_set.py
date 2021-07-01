from memoreminder.models import Tag
from memoreminder.serializers import TagSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class TagModelViewSet(TokenModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
