from django import forms
from .models import Carro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'ano', 'preco', 'cor', 'quilometragem', 'descricao', 'imagem']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']