from django.urls import path
from .views import SignUpView, ProfilView, LoginUser
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('profil/', views.ProfilView, name='profil_user')
]
