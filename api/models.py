from django.db import models

class Client(models.Model):
    ClientID = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Type = models.CharField(max_length=50)
    Coordonnees = models.TextField()

class Contrat(models.Model):
    ContratID = models.AutoField(primary_key=True)
    DateSignature = models.DateField()
    Statut = models.CharField(max_length=50)
    Client = models.ForeignKey(Client, related_name="contrats", on_delete=models.CASCADE)

class Evenement(models.Model):
    EvenementID = models.AutoField(primary_key=True)
    NomEvenement = models.CharField(max_length=100)
    DateDebut = models.DateField()
    DateFin = models.DateField()
    Statut = models.CharField(max_length=50)
    Contrat = models.ForeignKey(Contrat, related_name="evenements", on_delete=models.CASCADE)

class Utilisateur(models.Model):
    UtilisateurID = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Role = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)

class EquipeSupport(models.Model):
    Utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    Responsable = models.BooleanField(default=False)

    class Meta:
        unique_together = ('Utilisateur', 'Evenement')
