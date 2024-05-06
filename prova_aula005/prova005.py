# Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.

def calculando_media(lista):
    if len(lista) == 0:
        return 0  
    soma = sum(lista)  
    media = soma / len(lista)  
    return media
num = [13, 27, 14, 31, 87]
r = calculando_media(num)
print("A média dos números é:", r)