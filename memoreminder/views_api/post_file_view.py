from memoreminder.models import PostFile
from memoreminder.serializers import PostFileSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class PostFileModelViewSet(TokenModelViewSet):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')
