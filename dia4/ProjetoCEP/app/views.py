from django.shortcuts import render, redirect
import requests as api_requests #lembrar do pip install requests
from .forms import CepForm
from .models import  Endereco
# Create your views here.
def consulta_cep(request):
    form = CepForm()
    endereco = None
    erro = None
    
    if request.method == 'POST':
        form = CepForm(request.POST)
        if form.is_valid():
            cep = form.cleaned_data['cep']

            response = api_requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            dados_cep = response.json()

            if 'erro' not in dados_cep:

                endereco = Endereco(
                    rua=dados_cep.get('logradouro', ' '),
                    bairro= dados_cep.get('bairro', ' '),
                    cidade=dados_cep.get('localidade', ' '),
                    estado= dados_cep.get('uf', ' '),
                    cep=dados_cep.get('cep', ' '),
                    
                )
                endereco.save()

                return render(request, 'consulta_cep.html', {'form': form, 'endereco': endereco})
def home(request):
    form = CepForm()
    return render(request, 'home.html', {'form': form})