from rest_framework import serializers
from django.db.models import fields
from profiles_api import models
from .models import Medicamentos


class HelloSerializer(serializers.Serializer):
    """Serializa un campo para probar nuestro apiview"""
    name= serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializa obj de perfil de usuario"""

    class Meta:
        model = models.userProfile
        fields = ('id','email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self,validated_data):
        """Crear y retonar nuevo usuario"""
        user = models.userProfile.objects.create_user(
            email = validated_data ['email'],
            name = validated_data ['name'],
            password = validated_data['password']
        )
        return user
        
    def update(self, instance, validated_data):
        """Actualiza cuenta de usuario"""
        if 'password' in validated_data:
          password = validated_data.pop('password')
          instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializador de profile feedd items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = ('nombre', 'sub_categoria', 'cantidad')