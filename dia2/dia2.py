import math

# pip freeze > requirements.txt -> atualizar sempre p armazenar as dependencias necessarias p rodar o projeto


class FiguraGeometrica:
    def __init__(self):
        pass
        
    def areaCirculo(self, raio):
            
            

            return (raio ** 2)  * math.pi 
            
    def areaTriangulo(self, base, altura):
            areaT = (base * altura) / 2
        
            return areaT
    def hipotenusa(self,cateto1, cateto2):
            somacatetos = (cateto1 ** 2) + (cateto2 ** 2)
            valorhipotenusa = math.sqrt(somacatetos)

            return valorhipotenusa
    def arredondamento(numero: float) -> dict:
          
          return {
                "piso": math.floor(numero),
                "teto": math.ceil(numero),
                "arredondado": round(numero)
                
          }
                
          

calculadora = FiguraGeometrica()

while True:
            print("1 .CALCULAR AREA CIRCULO ")
            print("2 .CALCULAR AREA TRIANGULO ")
            print("3 .CALCULAR HIPOTENUSA ")
            print("4 .SAIR")

            escolha = input("Digite a opção desejada 1-4 ")

            if escolha == '1':
                raio = float(input("Digite o raio"))
                area = calculadora.areaCirculo(raio)
                print(area)


            elif escolha == '2':
                base = float(input("Digite a base"))
                altura = float(input("Digite a altura"))
                area = calculadora.areaTriangulo(base, altura)
                print(area)
            elif escolha == '3':
                cateto1 = float(input("Digite o primeiro cateto."))
                cateto2 = float(input("Digite o segundo cateto."))
                Hipotenusa = calculadora.hipotenusa(cateto1, cateto2)
                print(Hipotenusa)
            elif escolha == '4':
                break







