# print("Olá, mundo!"
# erro de sintaxe, faltou fechar o parenteses.

print("Olá, mundo!") # Fechando os parenteses.

# print(nome)
# NameError, uma das formas de ocorrer 
# um erro de variável nao definida, no caso, nome.

nome = "Renan"
print(nome) # corrigindo o erro 
# declarando e definindo a variável "nome"

#def somar(a, b): erro de tipagem, a variavel resultado
 #   return a + b  | tenta somar um numero (10), com a string "5"

#resultado = somar(10, "5") ----> onde está o erro exatamente.
#print(resultado)

def somar(a, b):
    try:
        
        return a + b
    except TypeError:
        return  "Erro: Não é possível realizar a soma de um número por Caractér."
resultado = somar(10, "5")
print(resultado)

# numeros = [10, 20, 30]
# indice = int(input("Digite um índice para acessar a lista: ")) 
#
# print(numeros[indice])
# Aqui é um erro que ocorre com o input do usuário,
# Sendo necessário usar tratamento de erro e uma forma de impedir
# que o usuário insira um indice invalido



numeros = [10, 20, 30]
while True: # while true ---> enquanto o indice for válido, executará o código até que a entrada seja valida
    

    try:
        indice = int (input("Digite um índice para acessar a lista: "))
        print(numeros[indice])
        break 
    except (IndexError, ValueError): # ValueError caso o usuário insira outra entrada que não seja inteiro.
        print("Erro: índice inválido, insira um número inteiro de 0 a 2.") # instruindo o usuário a usar indices válidos

#def dividir(a, b): pode gerar erro de valueerror, quando insere um valor inválido, e zerodivisionerror, quando insere uma divisao por 0
    #while True:
     #   try:
      #      return a / b
      #  except:


#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")

#resultado = dividir(int(num1), int(num2))
#print(f"Resultado: {resultado}")

def dividir(a, b): # PODE GERAR VALUEERROR, ZERODIVISIONERROR
    while True:
        try:
            return a / b
            
        except  ZeroDivisionError: # TRATANDO O ZERODIVISIONERROR
            print("Erro: Número inválido, insira um número inteiro e que não seja 0.")
            a = int(input("Digite o primeiro número novamente: "))
            b = int(input("Digite o segundo número novamente: "))
            
while True: # TRATANDO O VALUE ERROR DO INPUT.
    try:
        num1 = int(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Erro: por favor, digite um número inteiro váido")
        
while True:
    try:
        num2 = int(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Erro: por favor, digite um número inteiro váido")


resultado = dividir(int(num1), int(num2))


#dados = {
 #   "nome": "Isaac ",
 #   "idade": 25,
  #  "cidade": "São Paulo"
#}
#Aqui pode ocorrer key error no input do usuário
#chave = input("Digite a chave que deseja acessar: ")

#print(f"O valor da chave '{chave}' é: {dados[chave]}")





dados = { # O erro que pode ocorrer é no input do usuário, com key error
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

while True:
    chave = input("Digite a chave que deseja acessar: ")
    try:
        print(f"O valor da chave '{chave}' é: {dados[chave]}")
        break
    except KeyError:
        print("Insira uma chave válida, as possíveis são: nome, cidade e idade.")
        
chave2 = input("Digite a chave que deseja acessar: ")
valor = dados.get(chave2, "Chave não encontrada: ") # usando a funçao get (com ela nao precisa fazer try-except)
# estrutura do get padrao -> valor = dicionario.get(chave, valor_padrao)

print(f"O valor da chave '{chave2}' é: {valor}")

