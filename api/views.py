from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client, Contrat, Evenement, Utilisateur, EquipeSupport
from .serializers import (
    ClientSerializer, ContratSerializer, EvenementSerializer,
    UtilisateurSerializer, EquipeSupportSerializer
)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Nom', 'Coordonnees']
    ordering_fields = ['Nom']

class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.select_related('Client').all()
    serializer_class = ContratSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Statut', 'Client']

class EvenementViewSet(viewsets.ModelViewSet):
    queryset = Evenement.objects.select_related('Contrat').all()
    serializer_class = EvenementSerializer
    permission_classes = [permissions.IsAuthenticated]

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]

class EquipeSupportViewSet(viewsets.ModelViewSet):
    queryset = EquipeSupport.objects.select_related('Utilisateur', 'Evenement').all()
    serializer_class = EquipeSupportSerializer
    permission_classes = [permissions.IsAuthenticated]
