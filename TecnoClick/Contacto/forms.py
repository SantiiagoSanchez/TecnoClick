from django import forms


class FormContacto(forms.Form):
    Nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    Email = forms.EmailField(label="Email", required=True)
    Contenido = forms.CharField(label="Mensaje", max_length=200, required=True)