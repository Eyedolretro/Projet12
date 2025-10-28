from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ClientViewSet, ContratViewSet, EvenementViewSet, CommunicationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse

# -------------------------------
# Vue racine
# -------------------------------
def home(request):
    return JsonResponse({"message": "Bienvenue sur l'API Projet12"})

# -------------------------------
# Router DRF
# -------------------------------
router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'contrats', ContratViewSet)
router.register(r'evenements', EvenementViewSet)
router.register(r'communications', CommunicationViewSet)

# -------------------------------
# URLs
# -------------------------------
urlpatterns = [
    path('', home),  # racine /
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # endpoints DRF
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
