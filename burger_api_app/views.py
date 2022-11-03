from rest_framework.viewsets import ModelViewSet

from burger_api_app.models import UserProfile, Order, Address
from burger_api_app.serializers import UserProfileSerializer, OrderSerializer, AddressSeriaLizer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


# Create a OrderViewSet
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

# Create a Adderess ViewSets 
class AddressViewSets(ModelViewSet):
    serializer_class = AddressSeriaLizer
    queryset = Address.objects.all()
