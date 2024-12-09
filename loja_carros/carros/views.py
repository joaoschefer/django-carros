from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Carro 
from .forms import CarroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def public_home(request):
    if request.user.is_authenticated:
        return redirect('carros:home_private')  # Redireciona para a home privada
    return render(request, 'carros/home_public.html')  # Página pública
    
def private_home(request):
    return render(request, 'carros/home_private.html', {'user': request.user})

def custom_logout_view(request):
    logout(request)  
    return redirect('carros:home') 

def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carros/listar_carros.html', {'carros': carros})

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    return render(request, 'carros/detalhes_carro.html', {'carro': carro})

def cadastrar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carros:listar_carros')
    else:
        form = CarroForm()
    return render(request, 'carros/cadastrar_carro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('carros:home_private')  # Página privada após login
        else:
            messages.error(request, 'Credenciais inválidas')
            return render(request, 'autenticacao/login.html')

    return render(request, 'autenticacao/login.html')



def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Verificar se as senhas coincidem
        if password != password_confirm:
            messages.error(request, "As senhas não coincidem!")
            return render(request, 'autenticacao/cadastro.html')

        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return render(request, 'autenticacao/cadastro.html')

        # Verificar se o email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return render(request, 'autenticacao/cadastro.html')

        # Criar o usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Mensagem de sucesso
        messages.success(request, "Cadastro realizado com sucesso! Agora você pode fazer login.")
        return redirect('carros:login')  # Redireciona para a página de login

    return render(request, 'autenticacao/cadastro.html')