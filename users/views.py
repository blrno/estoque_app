from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm, CustomLoginForm


# View responsável por autenticar o usuário
class Login(LoginView):
    template_name = "users/login/index.html"   # Caminho do template de login
    form_class = CustomLoginForm               # Formulário personalizado de login
    success_url = "/"                          # Redirecionamento após login bem-sucedido


# View responsável por encerrar a sessão do usuário
class Logout(LogoutView):
    next_page = "/"                             # Redirecionamento após logout


# View para cadastro de novos usuários, acessível apenas por superusuários
class Register(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = "users/register/index.html" # Template do formulário de cadastro
    form_class = RegisterUserForm               # Formulário de criação de usuário
    success_url = "/users/login/"               # Redirecionamento após cadastro

    login_url = "/admin/login/"                 # Página de login caso acesse sem permissão
    redirect_field_name = None                  # Remove parâmetro ?next=

    def test_func(self):
        # Permite acesso somente se o usuário logado for superusuário
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Mantém o comportamento padrão ao não ter permissão
        return super().handle_no_permission()

    def form_valid(self, form):
        # Salva o usuário e processa o formulário se tudo estiver correto
        user = form.save()
        if user:
            return super().form_valid(form)
        else:
            # Retorna erro caso o formulário não seja válido
            return self.form_invalid(form)
