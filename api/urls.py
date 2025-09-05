# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientViewSet, ContratViewSet, EvenementViewSet,
    UtilisateurViewSet, EquipeSupportViewSet
)

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'contrats', ContratViewSet)
router.register(r'evenements', EvenementViewSet)
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'equipe-support', EquipeSupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
