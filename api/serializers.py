from rest_framework import serializers
from .models import UserData, Order, UserLanguage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class UserLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLanguage
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'