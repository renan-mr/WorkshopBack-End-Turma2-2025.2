from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #lembrar do pip install requests
from .forms import EnderecoForm, CepForm
from .models import  Endereco
import requests as api_requests
from django.shortcuts import render, redirect
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
class enderecoListView(ListView):
    model = Endereco
    template_name = 'endereco_list.html'
    context_object_name = 'enderecos'

class enderecoDetailView(DeleteView):
    model = Endereco
    template_name = 'endereco_detail.html'
    context_object_name = 'endereco'

class enderecoCreateView(CreateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'endereco_form.html'
    success_url = reverse_lazy('endereco_list')

class enderecoUpdateView(UpdateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'endereco_form.html'
    success_url = reverse_lazy('endereco_list')

class enderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'endereco_confirm_delete.html'
    success_url = reverse_lazy('endereco_list')