from rest_framework import serializers
from .models import Client, Contrat, Evenement, Utilisateur, EquipeSupport

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrat
        fields = "__all__"

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = "__all__"

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"

class EquipeSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeSupport
        fields = "__all__"
