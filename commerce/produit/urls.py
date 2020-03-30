from django.urls import path
from . import views


urlpatterns = [
    path('gestion/', views.gestion_boutique, name='gestion_boutique'),
    path('create/', views.ProduitCreate, name='produit_create'),
    path('list/', views.ProduitList, name='produit_list'),
    path('update/<int:produit_id>', views.ProduitUpdate, name="produit_update"),
    path('delete/<int:produit_id>', views.ProduitDelete, name="produit_delete"),
    path('categorie/', views.CategorieProduit, name='categorie_produit'),
    path('categorie/<categorie>', views.ProduitParCategorie, name='produit_par_categorie'),
    path('fiche/<int:produit_id>', views.FicheProduit, name='fiche_produit'),        
]
