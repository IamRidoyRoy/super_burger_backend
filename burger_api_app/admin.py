from django.contrib import admin
from .models import UserProfile, Order
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'user']
    class  Meta:
        model = Order
