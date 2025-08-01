from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from core.models import Emprestimo

class Command(BaseCommand):
    help = 'Envia e-mails para clientes com livros atrasados'

    def handle(self, *args, **kwargs):
        emprestimos_atrasados = Emprestimo.objects.all()
        emprestimos_atrasados = [e for e in emprestimos_atrasados if e.atrasado]

        for emprestimo in emprestimos_atrasados:
            assunto = f"Atraso na devolução do livro {emprestimo.livro.titulo}"
            mensagem = (
                f"Olá {emprestimo.cliente.nome},\n\n"
                f"Notamos que o livro '{emprestimo.livro.titulo}' "
                f"deveria ser devolvido em {emprestimo.data_devolucao_prevista}.\n"
                f"Multa atual: R$ {emprestimo.multa:.2f}\n\n"
                f"Por favor, realize a devolução o quanto antes."
            )
            send_mail(
                assunto,
                mensagem,
                'seuemail@gmail.com',
                [emprestimo.cliente.email],
                fail_silently=False,
            )
        self.stdout.write(self.style.SUCCESS('Notificações enviadas com sucesso!'))
