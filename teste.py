numeros = [1, 2,7, 4, 5,8,10]
for numero in numeros.copy():
    if numero % 2 == 0:
        numeros.remove(numero)

print(numeros)