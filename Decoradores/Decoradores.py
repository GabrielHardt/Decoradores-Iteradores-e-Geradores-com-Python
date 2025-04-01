# 📝 Exercício: Logger de Funções
# Crie um decorador chamado log_decorator que faz o seguinte:

# ✅ Aceita qualquer função com qualquer número de argumentos (*args, **kwargs).
# ✅ Exibe uma mensagem antes de chamar a função, informando qual função foi chamada e com quais argumentos.
# ✅ Exibe uma mensagem depois, informando o resultado da função.
# ✅ Usa functools.wraps para manter os metadados da função original.

import functools  # Importa a biblioteca functools para usar wraps e preservar metadados da função decorada.

# Definição do decorador
def log_decorator(func):
    @functools.wraps(func)  # Mantém os metadados da função original (nome, docstring, etc.)
    def wrapper(*args, **kwargs):  # Aceita qualquer número de argumentos posicionais e nomeados
        print(f"📌 Chamando: {func.__name__} com args={args} e kwargs={kwargs}")  
        # Exibe o nome da função e os argumentos passados a ela.

        resultado = func(*args, **kwargs)  # Chama a função original com os argumentos recebidos
        print(f"✅ Resultado de {func.__name__}: {resultado}")  
        # Exibe o resultado retornado pela função original

        return resultado  # Retorna o resultado da função original para não alterar seu comportamento
    return wrapper  # Retorna a função `wrapper`, que agora tem a lógica do decorador aplicada

# Função soma que será decorada
@log_decorator  # Aplica o decorador log_decorator à função soma
def soma(a, b):
    return a + b  # Retorna a soma de dois números

# Função saudação que será decorada
@log_decorator  # Aplica o decorador log_decorator à função saudacao
def saudacao(nome, mensagem="Olá"):
    return f"{mensagem}, {nome}!"  # Retorna uma saudação personalizada

# Teste da função soma
print(soma(3, 5))  
# 📌 Chamando: soma com args=(3, 5) e kwargs={}
# ✅ Resultado de soma: 8
# 8

# Teste da função saudacao com argumento padrão
print(saudacao("Alice"))
# 📌 Chamando: saudacao com args=('Alice',) e kwargs={}
# ✅ Resultado de saudacao: Olá, Alice!
# Olá, Alice!

# Teste da função saudacao com argumento nomeado
print(saudacao("Bob", mensagem="Bom dia"))
# 📌 Chamando: saudacao com args=('Bob',) e kwargs={'mensagem': 'Bom dia'}
# ✅ Resultado de saudacao: Bom dia, Bob!
# Bom dia, Bob!

# OBS : Se você não retornar o resultado dentro do wrapper, a função decorada não retornará nada (None), quebrando seu comportamento 
# esperado.