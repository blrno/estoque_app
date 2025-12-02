from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


# Formulário de login personalizado
class CustomLoginForm(AuthenticationForm):
    # Campo de nome de usuário com placeholder no input
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu usuário",
            }
        )
    )

    # Campo de senha com placeholder e mascaramento do input
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
            }
        ),
        label="Senha"
    )


# Formulário de registro de usuário baseado no UserCreationForm
class RegisterUserForm(UserCreationForm):
    # Campo de nome de usuário com placeholder
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Digite nome de usuário"})
    )

    # Primeira senha com placeholder
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Digite senha"}),
        label="Senha"
    )

    # Confirmação da senha com placeholder
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirme senha"}),
        label="Confirmar"
    )

    class Meta:
        model = User                       # Modelo utilizado no formulário
        fields = ("username", "password1", "password2")  # Campos exibidos no form
