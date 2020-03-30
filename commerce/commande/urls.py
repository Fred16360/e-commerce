from django.urls import path
from . import views


urlpatterns = [
    path('panier/', views.PanierView, name='panier'),
    path('panier/vider/', views.ViderPanier, name='vider_panier'),
    path('panier/valider/', views.ValiderCommande, name='valider_commande'),

]