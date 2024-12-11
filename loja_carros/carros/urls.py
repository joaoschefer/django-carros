from django.urls import path
from . import views

app_name = 'carros'

urlpatterns = [
    path('', views.public_home, name='home'),
    path('dashboard/', views.private_home, name='home_private'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('lista/', views.listar_carros, name='listar_carros'),
    path('<int:carro_id>/', views.detalhes_carro, name='detalhes_carro'),
    path('cadastrar/', views.cadastrar_carro, name='cadastrar_carro'),
]
