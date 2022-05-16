from email import message
from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers, models, permissions
from .models import Medicamentos





class HelloApi(APIView):
    """API VIEW DE PRUEBA"""
    serializer_class = serializers.HelloSerializer
    def get (self, request, format=None):
        """Retonar lista de características del API view"""

        an_apiview = [
            'USAMOS METDOS HTTP COMO FUNCIONES (GET,POST,PATCH,PUT,DELETE)',
            'ES SIMILAR A UNA VISTA TRADICIONAL DE DJANGO',
            'ESTA MAPEADO MANUALMENTE A LOS URLS',
        ]
        return Response({'message': 'Hola', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'Message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put (self, request, pk=None):
        """Maneja actualizar un objeto"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Maneja actualizacion parcial de un objeto"""

        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """BORRA UN OBJETO"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """TEST  API VIEW SET"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [


        ]
        return Response({'message': 'Hola!', 'a_viewset': a_viewset})

    def create(self, request):
        """Crear nuevo mensaje de hola mundo"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve (self, request, pk=None):
        """Obtiene el objeto y su id"""
        return Response({'http_method': 'GET'})

    def update (self, request, pk=None):
        """Actualiza un objeto"""

        return Response({'http_method': 'PUT'})

    def partial_update (self, request, pk=None):
        """Actualiza un objeto"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destruye un objeto"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Crear y actualizar perfiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.userProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):

    """Crea tokens de autenticacion de usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Maneja el Crear, Leer, Actualizar el profile feed"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
         IsAuthenticated
         )


    def perform_create (self, serializer):
        """Setea el perfil de usuario para el usuario que esta logeado"""
        serializer.save(user_profile = self.request.user)
class MedicamentosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicamentosSerializer
    queryset = Medicamentos.objects.all()

    def retrieve(self, request, pk=None):
        Medicamentos = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.MedicamentosSerializer(Medicamentos)
        return Response(serializer.data)
      

    