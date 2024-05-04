from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pesquisa.as_view(), name='pesquisa'),
    path('pedido/<int:pk>/', views.Consulta.as_view(), name='pedido'),
    path('pedidos/', views.ListaConsulta.as_view(), name='pedidos'),
    path('cadastroPedidos/', views.CadastroPedidos.as_view(), name='cadastroPedidos'),
    path('editar/', views.Editar.as_view(), name='editar'),
    path('delete/', views.Deletar.as_view(), name='delete'),
]
