# Considere o seguinte trecho de código em Python:

# import random



# lista = [1, 2, 3, 4, 5]

# x = random.choice(lista)



# a) Explique o que o código faz.

# b) Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive).

# c) Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive).

# a) Explique o que o código faz.
# RESPOSTA
# O trecho de código importa o módulo random, que fornece funções para gerar números aleatórios. Em seguida, cria uma lista chamada lista que contem os números de 1 a 5. A linha x = random.choice(lista) seleciona aleatoriamente um elemento da lista lista e atribui seu valor à variável x

# b) Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive)
# RESPOSTA
import random

numero_aleatorio = random.randint(10, 20)
print(numero_aleatorio)

# c) Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive).
# RESPOSTA
import random

lista_aleatoria = [random.randrange(1, 101) for _ in range(5)]
print(lista_aleatoria)

