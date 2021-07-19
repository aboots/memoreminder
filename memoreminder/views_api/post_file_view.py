from memoreminder.models import PostFile
from memoreminder.serializers import PostFileSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class PostFileModelViewSet(TokenModelViewSet):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer

    def get_serializer_context(self):
        context = super(PostFileModelViewSet, self).get_serializer_context()
        post = self.request.query_params.get('post', None)
        if post:
            context['post'] = post
        return context

    def pre_save(self, obj):
        if self.request.FILES.get('file'):
            obj.file = self.request.FILES.get('file')
