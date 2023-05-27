from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CourseViewSet, TagViewSet, ObtainAuthToken


router = DefaultRouter()

router.register('users', UserViewSet)
router.register('courses', CourseViewSet)
router.register('tags', TagViewSet)

app_name = 'api'
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/login/', ObtainAuthToken.as_view(), name='login'),
]
