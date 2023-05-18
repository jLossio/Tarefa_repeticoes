soma = 0

while True:
    n = int(input("Digite um numero para somar ou um numero negativo para sair: "))

    if n < 0:
        break
    soma += n  
print(soma)     