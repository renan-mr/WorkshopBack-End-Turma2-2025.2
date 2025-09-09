from django.db import models



# Create your models here.
class Endereco(models.Model):
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    cep = models.CharField(max_length=9) # length 9 pq sao 9 digitos
    
def __str__ (self):
    return f"{self.rua}, {self.cidade}"