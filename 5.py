candidatos = {
    1: "Jair Rodrigues",
    2: "Carlos Luz",
    3: "Neves Rocha"
}

votos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

total_votos = 0

while True:
    print("As opcoes sao:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("Entre com o seu voto: ")

    voto = int(input())

    if voto == 6:
        break
    elif voto >= 1 and voto <= 5:
        votos[voto] += 1
        total_votos += 1
    else:
        print("Voto invalido. Tente novamente.")

print("Resultado da eleicao:")
print("--------------------")

for candidato, nome in candidatos.items():
    num_votos = votos[candidato]
    porcentagem_votos = (num_votos / total_votos) * 100
    print(f"Candidato {nome}: {num_votos} votos ({porcentagem_votos:.2f}%)")

num_votos_nulos = votos[4]
porcentagem_nulos = (num_votos_nulos / total_votos) * 100
print(f"Votos nulos: {num_votos_nulos} votos ({porcentagem_nulos:.2f}%)")

num_votos_brancos = votos[5]
porcentagem_brancos = (num_votos_brancos / total_votos) * 100
print(f"Votos em branco: {num_votos_brancos} votos ({porcentagem_brancos:.2f}%)")

vencedor = max(votos, key=votos.get)
print(f"Candidato vencedor: {candidatos[vencedor]}")
