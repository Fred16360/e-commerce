from django import forms
from .models import DetailsCommande, Panier


class DetailsCommandeForm(forms.ModelForm):
    class Meta:
        model = DetailsCommande
        fields = '__all__'


class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['quantite']
    quantite = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "value": "1"
        })
    )
    

