from django.contrib import admin
from .models import UserData, UserLanguage, Order
admin.site.register((UserData, UserLanguage, Order))
