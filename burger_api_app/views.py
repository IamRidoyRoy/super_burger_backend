from rest_framework.viewsets import ModelViewSet

from burger_api_app.models import UserProfile, Order
from burger_api_app.serializers import UserProfileSerializer, OrderSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


# Create a OrderSerializer 
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()