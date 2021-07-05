from memoreminder.models import FriendRequest
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class FriendRequestSerializer(BaseTokenSerializer):
    memo_user_field_name = 'from_user'

    class Meta:
        model = FriendRequest
        fields = '__all__'

        read_only_fields = ('id', 'created')
