
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class UserForm(forms.ModelForm):
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        help_text=('Sua senha precisa ter no minimo 6 Caracter'),
        label='Senha'
    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirme sua senha',
    )

    class Meta:
        model = User
        fields = ('username',
                  'email', 'password', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        usuario_cadastro = cleaned_data.get('username')
        email_cadastro = cleaned_data.get('email')
        senha_cadastro = cleaned_data.get('password')
        senha2_cadastro = cleaned_data.get('password2')

        user = User.objects.filter(username=usuario_cadastro)
        email = User.objects.filter(email=email_cadastro)

        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'Email já existe'
        error_msg_psw = 'Senhas divergentes'
        error_msg_psw_short = 'Sua senha precisa ter no mínimo 6 caracteres'
        error_msg_psw_required = 'Este campo é obrigatório'

        if user:
            self.add_error('username', error_msg_user_exists)
        if email:
            self.add_error('email', error_msg_email_exists)

        if not senha_cadastro:
            self.add_error('password', error_msg_psw_required)
            self.add_error('password2', error_msg_psw_required)

        if senha_cadastro != senha2_cadastro:
            self.add_error('password', error_msg_psw)
            self.add_error('password2', error_msg_psw)
        if len(senha_cadastro) < 6:
            self.add_error('password', error_msg_psw_short)

        return cleaned_data
    