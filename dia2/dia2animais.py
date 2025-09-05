class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = str(idade)
        
    
    def falar(self):
        return "Som genérico"
    def apresentar(self):
        return self.nome + self.idade
    

class gato(animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        # pega o nome e idade de animal

    def falar(self):
        return "Miau Miau"
    
        

class cachorro(animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au Au"
class zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animais(self,animal):
        self.animais.append(animal)
    def listar_animais(self):
        for animal in self.animais:
            print(animal.apresentar())
    def listar_filtro(self,raca):
        for animal in self.animais:
            if isinstance(animal,raca):
                print(animal.apresentar())       
        
        '''dadosformatados = []
    
        for animal in self.animais:
            dados_do_animal = {
            "nome": animal.nome,
            "idade": animal.idade,
            "som": animal.falar(),
            "apresentacao": animal.apresentar()
        }
        dadosformatados.append(dados_do_animal)
        
        print(dadosformatados)
    
    def filtrar_por_tipo(self, raca):
         for animal in self.animais:
              if isinstance (animal, raca):
                
                print(animal)'''
         
meu_zoologico = zoologico()

gato1 = gato("Félix", 5)
cachorro1 = cachorro("Rex", 3)
gato2 = gato("Mimi", 2)

meu_zoologico.adicionar_animais(gato1)
meu_zoologico.adicionar_animais(cachorro1)
meu_zoologico.adicionar_animais(gato2)

meu_zoologico.listar_filtro(gato)
            


    
    
                