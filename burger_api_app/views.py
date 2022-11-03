from rest_framework.viewsets import ModelViewSet

from burger_api_app.models import UserProfile
from burger_api_app.serializers import UserProfileSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()