from django.db import models


# Create your models here.
class Produit(models.Model):
    reference = models.CharField(max_length=20, null=False, unique=True)
    categorie = models.CharField(max_length=20, null=False)
    titre = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    couleur = models.CharField(max_length=20, null=False)
    taille = models.CharField(max_length=5, null=False)
    PUBLIC_CHOIX = [('M', 'Homme'), ('F', 'Femme'), ('Mixte', 'Mixte')]
    public = models.CharField(choices=PUBLIC_CHOIX, max_length=5)
    photo = models.ImageField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.titre

