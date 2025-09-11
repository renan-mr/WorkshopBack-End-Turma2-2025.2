from django import forms
from .models import Endereco
class CepForm(forms.Form):
    cep = forms.CharField(label="CEP", max_length=9)

class EnderecoForm(forms.ModelForm): #importa o forms do proprio django pelo modelform
    class Meta: # nome meta por convençao do django  quando classes internas contem metadados
        model = Endereco
        fields = ['cep','cidade', 'estado', 'bairro', 'rua']