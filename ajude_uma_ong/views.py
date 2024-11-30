from django.shortcuts import render, get_object_or_404
from .models import ONG, Pauta

# Lista todas as ONGs
def listar_ongs(request):
    ongs = ONG.objects.all()
    return render(request, 'ajude_uma_ong/pautas/listar_ongs.html', {'ongs': ongs})

# Lista todas as pautas de uma ONG
def listar_pautas(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)
    pautas = ong.pautas.all()
    return render(request, 'ajude_uma_ong/pautas/listar_pautas.html', {'ong': ong, 'pautas': pautas})

# Exibe detalhes de uma pauta
def detalhes_pauta(request, pauta_id):
    pauta = get_object_or_404(Pauta, id=pauta_id)
    return render(request, 'ajude_uma_ong/pautas/detalhes_pauta.html', {'pauta': pauta})

