from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur l'API Projet12 !")

urlpatterns = [
    path('admin/', admin.site.urls),   # admin reste ici
    path('api/', include('api.urls')), # routes API
    path('', home),                    # page d'accueil
]
