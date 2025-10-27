from django.db import models
from django.contrib.auth.models import AbstractUser


class Equipe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



class Autorisation(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    equipe = models.ForeignKey(Equipe, related_name="autorisations", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} ({self.equipe.nom})"


class Utilisateur(AbstractUser):
    # Clé primaire personnalisée
    UtilisateurID = models.AutoField(primary_key=True)

    # Champs supplémentaires
    Email = models.EmailField(unique=True, default="inconnu@example.com")
    telephone = models.CharField(max_length=20, blank=True, null=True)
    equipe = models.ForeignKey(
        'Equipe', on_delete=models.SET_NULL, blank=True, null=True
    )

    # Supprimer id implicite : Django utilisera UtilisateurID
    # id = models.AutoField(primary_key=True) <-- NE PAS INCLURE

    def __str__(self):
        return self.username


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        default="inconnu@example.com"  # ✅ valeur par défaut si rien n’est fourni
    )
    telephone = models.CharField(max_length=20, blank=True, null=True)
    entreprise = models.CharField(max_length=100, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Contrat(models.Model):
    client = models.ForeignKey(Client, related_name="contrats", on_delete=models.CASCADE)
    date_signature = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrat #{self.id} - {self.client.nom}"


class Evenement(models.Model):
    contrat = models.ForeignKey(Contrat, related_name="evenements", on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} ({self.date.date()})"


class Communication(models.Model):
    client = models.ForeignKey(Client, related_name="communications", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    contenu = models.TextField()

    def __str__(self):
        return f"Com {self.client.nom} - {self.date.strftime('%Y-%m-%d')}"
