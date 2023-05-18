num = int(input("Entre com um valor:"))
#numero menor que ou igual 10
if num > 10:
    print ("Entre com outro valor")
else:
 #loop da tabuada   
    for i in range (1, 11):
        tabuada = num * i
        print (tabuada)
