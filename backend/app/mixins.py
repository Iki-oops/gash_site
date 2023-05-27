from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class UserModelMixin(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):
    pass
