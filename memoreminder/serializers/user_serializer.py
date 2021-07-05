from django.contrib.auth import password_validation

from memoreminder.models import MemoUser
from memoreminder.serializers import DynamicFieldModelSerializer


class MemoUserSerializer(DynamicFieldModelSerializer):
    class Meta:
        model = MemoUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'phone_number',
            'birthday_date',
            'friends',
            'created',
            'token',
        )

        read_only_fields = ('token', 'id', 'created')

    @staticmethod
    def validate_password(password):
        password_validation.validate_password(password)
        return password
