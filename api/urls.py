from django.urls import path, include
from rest_framework import routers
from api.views import ClientViewSet, ContratViewSet, EvenementViewSet, CommunicationViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'contrats', ContratViewSet)
router.register(r'evenements', EvenementViewSet)
router.register(r'communications', CommunicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
