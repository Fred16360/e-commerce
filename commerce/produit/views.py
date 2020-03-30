from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .models import Produit
from commande.models import Panier
from django.contrib.auth.models import User
from users.models import Client
from .forms import ProduitForm, ProduitFormUpdate
from commande.forms import PanierForm

# Create your views here.
def index(request):
    product = Produit.objects.all()
    return render(request, 'index.html', {'product': product})


def gestion_boutique(request):
    return render(request, 'gestion_boutique.html')


def ProduitList(request):
    return render(request, 'produit_list.html', {'produit_list': Produit.objects.all()})


def ProduitCreate(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProduitForm()
            return redirect('gestion_boutique')
    else:
        return render(request, "produit_add.html", {'form': form})


def ProduitUpdate(request, produit_id):
    produit_id = int(produit_id)
    try:
        produit_sel = Produit.objects.get(id=produit_id)
    except Produit.DoesNotExist:
        return redirect('produit_list')
    form = ProduitFormUpdate(request.POST or None, request.FILES or None, instance=produit_sel)
    if form.is_valid():
        form.save()
        return redirect('produit_list')
    return render(request, 'produit_update.html', {'form': form})


def ProduitDelete(request, produit_id):
    produit_id = int(produit_id)
    try:
        produit_sel = Produit.objects.get(id=produit_id)
    except Produit.DoesNotExist:
        return redirect('produit_list')
    produit_sel.delete()
    return redirect('produit_list')


def CategorieProduit(request):
    categorie = Produit.objects.order_by('categorie').values_list('categorie', flat=True).distinct()
    return render(request, 'categorie_produit.html', {'categorie_list': categorie})


def ProduitParCategorie(request, categorie):
    try:
        categorie_prod = Produit.objects.order_by('categorie').values_list('categorie', flat=True).distinct()
        categorie_sel = Produit.objects.filter(categorie=categorie)
    except Produit.DoesNotExist:
        return redirect('home')
    return render(request, 'produit_par_categorie.html', {'prod_par_cat': categorie_sel, 'categorie_list': categorie_prod})


def FicheProduit(request, produit_id):
    produit_id = int(produit_id)
    produit_sel = Produit.objects.get(id=produit_id)
    form = PanierForm()
    if request.method == 'POST':
        form = PanierForm(request.POST or None)
        if form.is_valid():
            form = Panier (
                membre=request.user,
                produit=produit_sel,
                quantite=form.cleaned_data["quantite"],
                prix=produit_sel.prix,
            )
            form.save()
            form = PanierForm()
            return redirect('panier')

    return render(request, 'fiche_produit.html', {'produit': produit_sel, 'panier': form})