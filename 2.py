#Codigo do numero secreto
import random

numero_secreto = random.randint(1, 100)

tent =  int(input("Digite sua tentativa: "))
#caso vc acerte de primeira
if numero_secreto == tent:
        print("Você acertou de primeira! O numero secreto era ", tent)
#loop
while numero_secreto != tent:
    tent =  int(input("Digite sua nova tentativa: "))
    
    if numero_secreto == tent:
        print("Você acertou! O numero secreto era ", tent)