from .models import Categorias, Comercios, Keywords, Transacciones
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comercios
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacciones
        fields = '__all__'
        extra_kwargs = {
            'description': {'required': False, 'allow_null': True},
            'amount': {'required': False, 'allow_null': True},
            'date': {'required': False, 'allow_null': True},
            'merchant': {'required': False, 'allow_null': True},
            'category': {'required': False, 'allow_null': True},
        }
