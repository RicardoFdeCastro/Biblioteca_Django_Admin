from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Cliente, Emprestimo

def meus_emprestimos(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    emprestimos = Emprestimo.objects.filter(cliente=cliente)
    return render(request, 'core/meus_emprestimos.html', {
        'cliente': cliente,
        'emprestimos': emprestimos
    })
