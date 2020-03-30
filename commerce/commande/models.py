from django.db import models
from users.models import Client
from produit.models import Produit
from datetime import date

# Create your models here.
class Commande(models.Model):
    membre = models.ForeignKey(Client, on_delete=models.CASCADE)
    montant = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    date_enregistrement = models.DateField(default=date.today)
    ETAT_CHOIX = [
        ('ENC', 'en cours de traitement'),
        ('ENV', 'envoyé'),
        ('LIV', 'livré'),
    ]
    etat = models.CharField(choices=ETAT_CHOIX, default='ENC', max_length=3)


class DetailsCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=False)
    quantite = models.PositiveSmallIntegerField(default=0)
    prix = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Panier(models.Model):
    membre = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.CASCADE)
    quantite = models.PositiveSmallIntegerField(default=1)
    prix = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    
