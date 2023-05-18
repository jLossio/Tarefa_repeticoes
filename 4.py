import random
jogadas = int(input("Quantas vezes você jogou a moeda? "))

for i in range(jogadas):
    resultado = random.randint(0, 1)
    
    if resultado == 1:
        resultado = ("Cara")
    else:
        resultado = ("Coroa")
    print (resultado)