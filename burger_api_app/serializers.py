from rest_framework.serializers import ModelSerializer
from burger_api_app.models import UserProfile, Order, Address

# Create a UserProfileSerializer to show json data 
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "email",
            "password",
        )
        # to change password i allow write only 
        extra_kwargs ={
            'password' : {'write_only': True, 'style': { 'input_type': 'password'}}
        }
 
    # Override the default create function as we used custom user model 
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user 

# Create a OrderSerializer class  
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


# Create a Address ModelSerializer 
class AddressSeriaLizer(ModelSerializer):
    class Meta: 
        model = Address
        fields = "__all__"
