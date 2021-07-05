from memoreminder.models import FriendRequest
from memoreminder.serializers import FriendRequestSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class FriendRequestModelViewSet(TokenModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        user_pk = self.get_serializer_context()['user']
        queryset = super(FriendRequestModelViewSet, self).get_queryset()
        return queryset.filter(to_user=user_pk)
