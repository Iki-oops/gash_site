from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, serializers
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from .models import Tag, Course, User
from .mixins import UserModelMixin
from .permissions import AnonUserPermission, CurrentUserPermission
from .serializers import (
    TagSerializer,
    CourseSerializer,
    EmailUsernameTokenLogin,
    UserSerializer,
    UserPostSerializer,
    ChangeUserInfoSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ('create'):
            return UserPostSerializer
        return UserSerializer

    @action(
        methods=['GET',],
        detail=False,
        permission_classes=[permissions.IsAuthenticated,])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['PATCH'],
        detail=False,
        permission_classes=[permissions.IsAuthenticated,],
        url_path='change-info')
    def change_info(self, request):
        serializer = ChangeUserInfoSerializer(request.user, data=request.data, partial=True)
        if not serializer.initial_data:
            raise serializers.ValidationError({'detail': 'Не передано поле'})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'Info success changed'}, status=status.HTTP_201_CREATED)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny,]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CurrentUserPermission,]


class ObtainAuthToken(APIView):
    permission_classes = [AnonUserPermission,]

    def post(self, request):
        serializer_class = EmailUsernameTokenLogin(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            email=serializer_class.validated_data.get('email')
        )
        check_password = user.check_password(
            serializer_class.validated_data.get('password')
        )
        if not check_password:
            return Response(
                data={'message': 'Пароль не совпадает'},
                status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        content = {'auth_token': token.key}
        return Response(content)
