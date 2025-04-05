# Crie uma classe chamada Contador que funciona como um iterador. Ela deve contar de um número inicial até um número final, um por vez.

# Regras:

# Use os métodos __iter__ e __next__.

# Quando passar do número final, deve levantar StopIteration.

class contador:
    def __init__(self, inicio, fim):
        self.atual = inicio #atual e inicio (pq comeca no atual)
        self.fim = fim
        
    def __iter__(self): # diz “aqui está um iterador que você pode usar para percorrer esse objeto”.
        return self
    
    def __next__(self):  #O __next__() funciona igualzinho a um loop for por baixo dos panos — ele retorna um valor por vez e pausa a       execução até que seja chamado novamente.
        if self.atual > self.fim:
            raise StopIteration
        valor = self.atual # por que precisamos passar o self.atual pra valor
        self.atual += 1 
        return valor 
    
contador = contador(1, 5) #Aqui esta sendo criado o objeto iterador, mas ainda precisa iterar sobre ele

for numero in contador: #for e quem faz as chamadas do next automaticamente
    print(numero)

