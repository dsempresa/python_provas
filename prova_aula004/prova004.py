# [PY-A04]Escreva uma função em Python que recebe dois números como argumentos e retorna o maior entre eles.

# a) Implemente a função com o nome "maior_numero" e utilizando condicionais.

# b) Implemente a mesma função, porém utilizando a função "max".

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b
    

def maior_numero(a, b):
    return max(a, b)