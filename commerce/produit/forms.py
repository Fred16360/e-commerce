from django import forms
from .models import Produit

PUBLIC_CHOIX = [('M', 'Homme'), ('F', 'Femme'), ('Mixte', 'Mixte')]

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
    reference = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    categorie = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    titre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "cols": "47",
            "rows": "3",
        })
    )
    couleur = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    taille = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    public = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control"
        }),
        choices=PUBLIC_CHOIX
    )
    prix = forms.CharField(
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        })
    )
    stock = forms.CharField(
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        })
    )
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "photo"
        })
    )


class ProduitFormUpdate(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
    reference = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    categorie = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    titre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "cols": "47",
            "rows": "3",
        })
    )
    couleur = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    taille = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    public = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control"
        }),
        choices=PUBLIC_CHOIX
    )
    prix = forms.CharField(
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        })
    )
    stock = forms.CharField(
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        })
    )        
    photo = forms.ImageField(
        required = False,
        widget=forms.FileInput(attrs={
            "class": "photo"
        })
    )