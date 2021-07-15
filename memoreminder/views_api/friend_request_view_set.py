from rest_framework.exceptions import PermissionDenied

from memoreminder.models import FriendRequest, MemoUser
from memoreminder.serializers import FriendRequestSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class FriendRequestModelViewSet(TokenModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    do_not_filter = True

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not token:
            raise PermissionDenied('user token missed')
        user = MemoUser.objects.filter(token=token).first()
        if not user:
            raise PermissionDenied('user token not found')
        queryset = super(FriendRequestModelViewSet, self).get_queryset()
        return queryset.filter(to_user=user)
