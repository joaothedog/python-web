from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viagem/<int:id>/', views.detalhes_viagem, name='detalhes_viagem'),
    path('viagem/nova/', views.nova_viagem, name='nova_viagem'),
    path('viagem/<int:viagem_id>/excluir/', views.excluir_viagem, name='excluir_viagem'),
    path('viagem/<int:viagem_id>/gasto/', views.adicionar_gasto_extra, name='adicionar_gasto_extra'),
]


