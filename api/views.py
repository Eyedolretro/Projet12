from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client, Contrat, Evenement, Utilisateur, EquipeSupport
from .serializers import (
    ClientSerializer, ContratSerializer, EvenementSerializer,
    UtilisateurSerializer, EquipeSupportSerializer
)

# Permission personnalisée
class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Seul le staff peut modifier, tout le monde peut lire.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Nom', 'Coordonnees']
    ordering_fields = ['Nom']

class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.select_related('Client').all()
    serializer_class = ContratSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Statut', 'Client']

class EvenementViewSet(viewsets.ModelViewSet):
    queryset = Evenement.objects.select_related('Contrat').all()
    serializer_class = EvenementSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class EquipeSupportViewSet(viewsets.ModelViewSet):
    queryset = EquipeSupport.objects.select_related('Utilisateur', 'Evenement').all()
    serializer_class = EquipeSupportSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
