
capital_inicial = float(input("Digite o valor inicial a ser guardado na poupança: "))
taxa_juros = 0.005  # 0,5% ao mês

for mes in range(1, 13):
    montante = capital_inicial * (1 + taxa_juros)**mes
    print("Mês", mes ,"Montante", "=", "R$", montante)
