from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Client(AbstractUser):
    CIVILITE_CHOIX = [('F', 'Femme'), ('M', 'Homme')]
    civilite = models.CharField(choices=CIVILITE_CHOIX, default='M', max_length=1)
    ville = models.CharField(max_length=20, null=False)
    code_postal = models.PositiveSmallIntegerField(default=0,null=False)
    adresse = models.CharField(max_length=50, null=False)
    statut = models.PositiveSmallIntegerField(default=0, null=False)
    

    def __str__(self):
        return self.username