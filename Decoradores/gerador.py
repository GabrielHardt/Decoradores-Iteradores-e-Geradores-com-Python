# Crie uma função geradora chamada pares_ate(n) que gere todos os números pares de 0 até n (inclusive, se for par).

# Regras:

# Use a palavra-chave yield.

# A função deve retornar um número por vez, sem criar uma lista.

# Pode ser usada com for ou com next().


def pares_ate(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for i in pares_ate(10):
    print(i)

#O gerador em si é um objeto iterável e também um iterador ao mesmo tempo. O for em Python automatiza a iteração por trás dos panos

#O for esconde o trabalho sujo de chamar iter() e next() pra você, e por isso funciona lindamente com geradores.