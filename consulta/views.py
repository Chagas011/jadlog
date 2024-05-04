from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from . models import Pedidos
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import CadastroForm
from django.contrib import messages

# Create your views here.


class Consulta(DetailView):
    template_name = 'consulta/consulta.html'
    model = Pedidos
    context_object_name = 'pedido'


class ListaConsulta(ListView):
    template_name = 'consulta/consultas.html'
    model = Pedidos
    context_object_name = 'pedidos'


class CadastroPedidos(FormView):
    template_name = 'consulta/cadastro.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': CadastroForm(request.POST or None)  # Passa os dados do POST, se houver, para o formulário
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']

        if form.is_valid():
            post = form.save()
            messages.success(self.request, 'Post enviado com sucesso')
            return redirect('pedido:pesquisa')
        else:
            # Se o formulário não for válido, devemos atualizar o contexto com o formulário inválido
            self.contexto['form'] = form
            return render(request, self.template_name, self.contexto)
    

class Editar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('editar consulta')


class Deletar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('deletar')


class Pesquisa(View):
    template_name = 'consulta/pesquisa.html'
    model = Pedidos

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        rastreio = request.POST.get('rastreio')
        try:
            codigo = Pedidos.objects.get(pk=rastreio)
        except Pedidos.DoesNotExist:
            # Se não encontrar, retorna para a página de pesquisa com uma mensagem de erro
            return render(request, self.template_name, {'erro': 'Pedido não encontrado.'})
        
        # Se encontrar o objeto, redireciona para a página de detalhes do pedido
        return redirect(reverse('pedido:pedido', kwargs={'pk': codigo.pk}))
