from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Client

CIVILITE_CHOIX = [('M', 'Homme'), ('F', 'Femme') ]

class ClientCreationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name', 'email', 'civilite', 'ville', 'code_postal','adresse')
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "exemple@gmail.com"
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "id": "password1",            
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "id": "password2"            
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    civilite = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={
            "class": "checkbox",
            "value": "M",
            "checked": "",
            "type": "radio"
            }),
        choices=CIVILITE_CHOIX,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    code_postal = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "pattern": "[0-9]{1,5}",
        })
    )
    ville = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "votre ville",
        })
    )
    adresse = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "votre adresse",
        })
    )

    

class ClientChangeForm(UserChangeForm):
    class Meta:
        model = Client
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


