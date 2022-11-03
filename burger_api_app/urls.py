from django.urls import path 
from rest_framework.routers import DefaultRouter

from burger_api_app.views import UserProfileViewSet

router = DefaultRouter()
router.register(r'user', UserProfileViewSet)

urlpatterns = [] + router.urls