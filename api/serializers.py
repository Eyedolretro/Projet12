# serializers.py
from rest_framework import serializers
from .models import *
from .models import Evenement

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrat
        fields = '__all__'

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'
        read_only_fields = ('date',)  # ✅ la date ne doit pas être envoyée dans le POST

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'
