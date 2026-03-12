from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.PortfolioListView.as_view(), name='portfolio'),
    path('postar-projeto/', views.ProjetoCreateView.as_view(), name='postar_projeto'),
    path('excluir-projeto/<int:pk>/', views.ProjetoDeleteView.as_view(), name='excluir_projeto'),
    path('excluir-certificado/<int:pk>/', views.CertificadoDeleteView.as_view(), name='excluir_certificado'),
    path('postar-certificado/', views.CertificadoCreateView.as_view(), name='postar_certificado'),
    path('configurador/', views.ConfiguradorView.as_view(), name='configurador'),
    path('leads/', views.LeadListView.as_view(), name='lead_list'),
    path('api/filtrar-projetos/', views.filtrar_projetos, name='filtrar_projetos'),
]
