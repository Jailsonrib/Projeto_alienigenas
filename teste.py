# import sys
# # numeros = [1, 2,7, 4, 5,8,10]
# # for numero in numeros.copy():
# #     if numero % 2 == 0:
# #         numeros.remove(numero)

# # print(numeros)
# lista = []
# contador = 1
# while True:
#     if contador > 10 :
#         break
#     lista.append(contador)
#     contador += 1
#     print(lista) 
#     lis = []
# cont = 10
# while True:
#     if cont == 0:
#         sys.exit()
#     lis.append(cont)
#     cont -= 1
#     print(lis)
# def binomial_coefficient(n, k):
    
#     if k == 0 or k == n:
#         return 1
#     return (n * binomial_coefficient(n - 1, k - 1)) // k

# result = binomial_coefficient(5, 2)
# # Printing the result
# print(result)

# def to_camel_case(s):
#     parts = s.split('_')
#     return parts[0] + ''.join(word.capitalize() for word in parts[1:])
       
    
        
        
# result = to_camel_case("hello_world")
# # Printing the result
# print(result)

def to_camel_case(s: str):
    words = s.split("_")
    
    for i, word in enumerate(words):
        if i != 0:
            words[i] = word.capitalize()
    
    return "".join(words)

# Calling the function
result = to_camel_case("hello_world")
print(result)  # helloWorld