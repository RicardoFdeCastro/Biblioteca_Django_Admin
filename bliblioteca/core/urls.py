from django.urls import path
from . import views

urlpatterns = [
    path('meus-emprestimos/<int:cliente_id>/', views.meus_emprestimos, name='meus_emprestimos'),
]
