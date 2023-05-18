p = int(input("Digite o primeiro valor: "))
u = int(input("Digite o ultimo valor: "))

if u < p:
    for i in range(p, u, - 1,):
        print(i)
else:
    for i in range(p, u, + 1):
        print (i)