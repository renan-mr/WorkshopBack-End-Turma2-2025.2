import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(detail=False, methods=['post'])
    def busca_cep(self,request):
        # busca o cep na api viacep
        cep = request.data.get('cep', None)
        if not cep:
            return Response({'erro: ' 'o campo "cep" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(cep) != 8: #checa se o cep tem 8 digitos
            return Response({'error': 'CEP inválido. Deve conter 8 dígitos'})
        
        try:
            #verifica se o endereco ja existe no db
            if Endereco.objects.filter(cep = cep).exists():
                return Response({'message': 'CEP já registrado.'}, status=status.HTTP_200_OK)
            
            url = f'https://viacep.com.br/ws/{cep}/json/' # request da apiviacep
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            endereco_data = response.json()

            if 'erro' in endereco_data:
                return Response ({'error': 'CEP NÃO ENCONTRADO'}, status=status.HTTP_404_NOT_FOUND)
            
            # molda os dados da api para o serializador
            data_para_salvar = {
                'cep': endereco_data.get('cep', ' '),
                'rua': endereco_data.get('logradouro', ' '),
                'bairro': endereco_data.get('bairro', ' '),
                'cidade': endereco_data.get('localidade', ' '),
                'estado': endereco_data.get('uf', ' '),
            }
            
            serializer = self.get_serializer(data=data_para_salvar)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as e:
            return  Response({'erro:' f'Erro ao conectar com a API ViaCep: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'erro:' f'Ocorreu um erro inesperado: {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)