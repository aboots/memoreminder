from memoreminder.models import FriendRequest
from memoreminder.serializers.base_token_serializer import BaseTokenSerializer


class FriendRequestSerializer(BaseTokenSerializer):
    memo_user_field_name = 'from_user'

    def to_representation(self, instance):
        data = super(FriendRequestSerializer, self).to_representation(instance)
        user = instance.from_user
        data['from_user'] = {'id': user.pk,
                             'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name
                             }
        return data

    class Meta:
        model = FriendRequest
        fields = '__all__'

        read_only_fields = ('id', 'created')
