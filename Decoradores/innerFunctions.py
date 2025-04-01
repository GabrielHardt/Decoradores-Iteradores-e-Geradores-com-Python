# Desafio: Criar uma função que gera saudação personalizada
# Crie uma função chamada gerar_saudacao que:

# Aceite um nome como argumento.

# Contenha uma inner function chamada saudar().

# saudar() deve acessar o nome e retornar uma saudação personalizada.

# gerar_saudacao deve retornar a função saudar, para que possamos chamá-la depois.

def gerar_saudacao(nome):
    def saudar():
        print(f"Me chamo {nome}")
    return saudar

gerar_saudacao("Gabriel")() 