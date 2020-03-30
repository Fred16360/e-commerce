from django.contrib import admin
from .models import Produit

# Register your models here.
class ProduitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produit, ProduitAdmin)