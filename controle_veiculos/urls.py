from django.contrib import admin
from django.urls import path

import app_controle.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", views.home, name="home"),
    path("motorista_list/", views.MotoristaListView.as_view(), name="motorista_list"),
    path("veiculo_list/", views.VeiculoListView.as_view(), name="veiculo_list"),
    path("motorista_create/", views.MotoristaCreateView.as_view(), name="motorista_create"),
    path("veiculo_create/", views.VeiculoCreateView.as_view(), name="veiculo_create"),
    path("motorista_update/<int:pk>", views.MotoristaUpdateView.as_view(), name="motorista_update"),
    path("veiculo_update/<int:pk>", views.VeiculoUpdateView.as_view(), name="veiculo_update"),
    path("motorista_delete/<int:pk>", views.MotoristaDeleteView.as_view(), name="motorista_delete"),
    path("veiculo_delete/<int:pk>", views.VeiculoDeleteView.as_view(), name="veiculo_delete"),
    path("", views.ControleListView.as_view(), name="controle_list"),
    path("controle_create/", views.ControleCreateView.as_view(), name="controle_create"),
    path("controle_update/<int:pk>", views.ControleUpdateView.as_view(), name="controle_update"),
    path("controle_delete/<int:pk>", views.ControleDeleteView.as_view(), name="controle_delete"),
    path("controle_detail/<int:pk>", views.ControleDetailView.as_view(), name="controle_detail"),
]
