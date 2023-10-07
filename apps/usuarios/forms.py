from django import forms

class LoginForm(forms.Form):

    nome_login = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seu login aqui...',
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Sua senha aqui...',
            }
        )
    )

