from rest_framework import serializers, validators
from users.models import CustomUser
from rest_framework.serializers import ValidationError
from django.contrib.auth.hashers import make_password
from .validators.password import PasswordValidator


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'bio')

        extra_kwargs = {
            'password1': {
                'write_only': True,
                'validators': [
                    PasswordValidator()
                ]
            },
            'password2': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(CustomUser.objects.all(), 'This email already exists!'),
                ]
            },
            'bio': {
                'allow_blank': True,
                'required': False,
            }
        }

    def validate(self, attrs):
        if attrs.get('password1') != attrs.get('password2'):
            raise ValidationError("Passwords don't match!")
        else:
            return attrs

    def create(self, validated_data):
        username = validated_data.get('username')
        password_1 = validated_data.get('password1')
        password_2 = validated_data.get('password2')
        email = validated_data.get('email').lower()
        bio = validated_data.get('bio')

        user = CustomUser.objects.create(
            username=username,
            password=make_password(password_1, hasher='default'),
            email=email,
            bio=bio
        )
        return user
