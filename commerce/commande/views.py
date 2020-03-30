from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Panier, Commande, DetailsCommande
from produit.models import Produit
from users.models import Client


# Create your views here.
@login_required
def PanierView(request):
    panier_sel = Panier.objects.filter(membre_id=request.user)
    montanttotal = MontantTotal(request)
    return render(request, 'panier.html', {'panier': panier_sel, 'total': montanttotal})


def ViderPanier(request):
    panier_sel = Panier.objects.filter(membre_id=request.user)
    for panier in panier_sel:
        panier.delete()
        panier_sel = Panier.objects.filter(membre_id=request.user)
    return render(request, 'panier.html', {'panier': panier_sel})


def MontantTotal(request):
    panier_sel = Panier.objects.filter(membre_id=request.user)
    total = 0
    for panier in panier_sel:
        total += panier.prix * panier.quantite
#        b=Panier.objects.get(id=panier.id)
#        b.total=total
#        b.save()
    return total


def ValiderCommande(request):
    panier_sel = Panier.objects.filter(membre_id=request.user)
    total = MontantTotal(request)
    commande = Commande(
        membre=request.user,
        montant=total,
    )
    commande.save()
    paniervalid=None
    for panier in panier_sel:
        paniervalid = DetailsCommande(
            commande=commande,
            produit=panier.produit,
            quantite=panier.quantite,
            prix=panier.prix
        )
        paniervalid.save()
    return redirect('vider_panier')