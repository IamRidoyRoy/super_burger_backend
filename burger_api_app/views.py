from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from burger_api_app.models import UserProfile, Order, Address
from burger_api_app.serializers import UserProfileSerializer, OrderSerializer, AddressSeriaLizer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


# Create a OrderViewSet
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [
        # IsAuthenticated
    ]

    # Override the default queryset filtering 
    def get_queryset(self):
        queryset = Order.objects.all()
        id = self.request.query_params.get("id", None)
        if id is not None:
            queryset = queryset.filter(user__id=id)

        return queryset

# Create a Adderess ViewSets 
class AddressViewSets(ModelViewSet):
    serializer_class = AddressSeriaLizer
    queryset = Address.objects.all()
