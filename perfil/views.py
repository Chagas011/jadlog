from .formularios import UserForm
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class Criar(FormView):
    template_name = 'perfil/cadastro.html'
    form_class = UserForm
   
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
           
            form.save()
            return self.form_valid(form)
        else:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return self.form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Você fez Cadastro com sucesso')
        return redirect('perfil:login')


class Login(View):
    template_name = 'perfil/login.html'

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('perfil:criar')

        usuario = authenticate(
            self.request, username=username, password=password
        )

        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('perfil:criar')
        login(self.request, user=usuario)
        messages.success(
            self.request,
            'Você fez login com sucesso'
        )
        return redirect('pedido:cadastroPedidos')


class Logout(FormView):
    pass
