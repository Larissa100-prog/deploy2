from django.urls import path
from . import views

urlpatterns = [
    path('ongs/', views.listar_ongs, name='listar_ongs'),
    path('ongs/<int:ong_id>/pautas/', views.listar_pautas, name='listar_pautas'),
    path('pautas/<int:pauta_id>/', views.detalhes_pauta, name='detalhes_pauta'),
]