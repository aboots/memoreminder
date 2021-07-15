from django.contrib.auth import password_validation
from rest_framework import serializers

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


class ListMemoUserSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        raise serializers.ValidationError('قادر به ویرایش کاربران به صورت گروهی نیستید.')

    class Meta:
        model = MemoUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'friends',
            'phone_number',
        )

        read_only_fields = ('token', 'id', 'created')
