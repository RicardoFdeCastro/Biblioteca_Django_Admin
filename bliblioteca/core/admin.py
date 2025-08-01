from django.contrib import admin
from .models import Funcionario, Cliente, Livro, Emprestimo
from django.db.models import Count
from django.utils.html import format_html

# Register your models here.


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_admissao']
    search_fields = ['nome', 'email']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_cadastro']
    search_fields = ['nome', 'email']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editora', 'ano_publicacao', 'quantidade']
    search_fields = ['titulo', 'autor']


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'livro', 'data_retirada', 'data_devolucao_prevista', 'data_devolucao_real', 'multa']
    list_filter = ['data_retirada', 'data_devolucao_prevista']

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'livro', 'data_retirada', 'data_devolucao_prevista', 'data_devolucao_real', 'multa']

    change_list_template = "admin/emprestimos_changelist.html"

    def changelist_view(self, request, extra_context=None):
        livros_populares = (
            self.model.objects
            .values('livro__titulo')
            .annotate(total=Count('id'))
            .order_by('-total')[:5]
        )
        extra_context = extra_context or {}
        extra_context['livros_populares'] = livros_populares
        return super().changelist_view(request, extra_context=extra_context)