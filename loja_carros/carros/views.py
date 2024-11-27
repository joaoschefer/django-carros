from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro
from .forms import CarroForm

# view para pagina home
def home(request):
    return render(request, 'carros/home.html')

# view que vai listar os carros
def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carros/listar_carros.html', {'carros': carros})

# view que vai exibir detalhes de um carro especifico
def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    return render(request, 'carros/detalhes_carro.html', {'carro': carro})

# view para cadastrar um novo carro
def cadastrar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carros:listar_carros')
    else:
        form = CarroForm()
    return render(request, 'carros/cadastrar_carro.html', {'form': form})
