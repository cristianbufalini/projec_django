from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True,widget=forms.TextInput(attrs={'class': 'form-control' }) )
    first_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control' }))
    last_name = forms.CharField(label='Apellido', required=True, widget=forms.TextInput(attrs={'class': 'form-control' }))
    username = forms.CharField(label='Nombre de usuario', required=True, widget=forms.TextInput(attrs={'class': 'form-control' }))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'  }), required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'  }), required=True )
    imagen = forms.ImageField(label='Imagen', required=False, widget=forms.TextInput(attrs={'class': 'form-control'  }))

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'imagen',
        ]
