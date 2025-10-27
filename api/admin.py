from django.contrib import admin
from .models import Client, Contrat, Evenement, Utilisateur, Equipe


# Enregistrer chaque modèle pour l'admin
admin.site.register(Client)
admin.site.register(Contrat)
admin.site.register(Evenement)
admin.site.register(Utilisateur)
admin.site.register(Equipe)
