from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ClientCreationForm, LoginForm
from .models import Client


# Create your views here.
class SignUpView(CreateView):
    form_class = ClientCreationForm
    success_url = reverse_lazy('login_user')
    template_name = 'signup.html'


class LoginUser(LoginView):
    template_name = 'registration/login.html'  # your template
    form_class = LoginForm  # your form


@login_required
def ProfilView(request):
    return render(request, "profil.html", {})
        