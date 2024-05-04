from .formularios import UserForm, LoginForm
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.urls import reverse



class Criar(FormView):
    template_name = 'perfil/cadastro.html'
    form_class = UserForm
    success_url = reverse_lazy('perfil:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Seu formulário foi enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro no envio do formulário. Por favor, corrija os erros e tente novamente.')

        # Retornar a resposta padrão do método form_invalid
        return super().form_invalid(form)


class Login(FormView):
    template_name = 'perfil/login.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': LoginForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Dados invalidos')

        authenticated_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('pedido:cadastroPedidos'))
        else:
            messages.error(request, 'Usuario ou senha invalidos')

        return render(request, self.template_name, self.contexto)


class Logout(FormView):
    pass
