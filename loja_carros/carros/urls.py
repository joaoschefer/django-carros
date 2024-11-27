from django.urls import path
from . import views

app_name = 'carros'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.listar_carros, name='listar_carros'),
    path('<int:carro_id>/', views.detalhes_carro, name='detalhes_carro'),
    path('cadastrar/', views.cadastrar_carro, name='cadastrar_carro'),
]
