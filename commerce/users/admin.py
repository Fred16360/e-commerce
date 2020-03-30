from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ClientCreationForm, ClientChangeForm
from .models import Client


# Register your models here.
class ClientAdmin(UserAdmin):
    add_form = ClientCreationForm
    form = ClientChangeForm
    model = Client
    list_display = ('email', 'username',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'civilite', 'ville', 'code_postal', 'adresse',)}),
    )

admin.site.register(Client, ClientAdmin)