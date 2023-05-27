from rest_framework import serializers

from .fields import Base64ImageField
from .models import Tag, Course, User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'description',
            'avatar',
        )

    def get_avatar(self, obj):
        return '/media/' + obj.avatar.name


class UserPostSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'description',
            'avatar',
            'password',
        )
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ChangeUserInfoSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField()

    class Meta:
        model = User
        fields = (
            'avatar',
            'username',
            'first_name',
            'last_name',
            'bio',
            'description'
        )


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('pk', 'name', 'hex_color')


class CourseSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'pk', 'name', 'description', 'tags', 'created_at', 'updated_at',
        )


class EmailUsernameTokenLogin(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
        }

    def validate(self, data):

        return data
