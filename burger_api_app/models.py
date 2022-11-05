import email
from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
# Create your models here.

# Create a new user 
class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("The user must have a email")

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)
         
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

    

# Now i am creating a custom user model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique= True)
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_new_user = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default= False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email




# # Create new model class Ingredients 
# class Ingredients(models.Model):
#     salad = models.TextField(max_length=100, blank = False)
#     cheese = models.TextField(max_length=100)
#     meat = models.TextField(max_length=100)
#     chicken = models.TextField(max_length=100)

    
# Create a Order class to see order 
from django.conf import settings
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    product_name = models.TextField(max_length= 100, blank = False , null = False)
    price = models.TextField(max_length=100, blank=False)
    order_time = models.DateTimeField(auto_now=True)
    salad = models.TextField(max_length=100, blank = True)
    cheese = models.TextField(max_length=100,  blank = True)
    meat = models.TextField(max_length=100,  blank = True)
    chicken = models.TextField(max_length=100,  blank = True)
    

    def __str__(self) :
        return self.product_name


# Create a model fore Address 
class Address(models.Model):
    address = models.TextField(max_length= 500, blank=False, null = False)

    def __str__(self):
        return self.address