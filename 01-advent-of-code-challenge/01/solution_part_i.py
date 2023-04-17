with open('sample.in', 'r') as f:
    arquivo = f.readlines()

calorias_totais = []
elfo_atual = []
for linha in arquivo:
    if linha.strip() == '':
        calorias_totais.append(elfo_atual)
        elfo_atual = []
    else:
        elfo_atual.append(int(linha.strip()))

totals = [sum(caloria) for caloria in calorias_totais]

print(max(totals))