import json

total = 0
quantidade = 0
contaFixa = 0

#salva os arquivos sem apagar os anteriores:
try:
    with open("contas.json", "r") as conta:
        contas = json.load(conta)
except:
    contas = []

# Percorre as contas carregadas do JSON para atualizar quantidade, total e contas fixas
for conta in contas:
    quantidade += 1
    total += conta["valor"]

    if conta["fixa"] == "sim":
        contaFixa += 1

conta = str.lower(input("Deseja cadastrar a conta? "))

while conta == "sim":
    nome = str.lower(input("Nome da conta: "))
    data = int(input("Informe a dia do vencimento: "))
    mes = int(input("Informe o mês do vencimento: "))
    valor = float(input("Valor da conta: "))

    if ((data >=1 and data <=31) and (mes >=1 and mes<=12)):
        print("data valida")
        quantidade += 1
        total += valor
    else: 
        print("data inválida")

    fixa = str.lower(input("esta conta é fixa? "))
    if fixa == "sim":
        contaFixa+=1

    contaAtual={
        "nome": nome,
        "dia": data,
        "mes": mes,
        "valor": valor,
        "fixa": fixa
    }
#adiciona os dados na array  
    contas.append(contaAtual)

    conta = str.lower(input("Deseja cadastrar outra conta? "))

#salva os dados novos no json
with open("contas.json", "w") as conta:
    json.dump(contas, conta, indent=4)

#percorre as informações das contas e exibe
for conta in contas:
    print(f"Nome: {conta['nome']}")
    print(f"Vencimento: {conta['dia']}/{conta['mes']}")
    print(f"Valor: R$ {conta['valor']:.2f}")
    print(f"Fixa: {conta['fixa']}")
    print("-" * 30)

print(f"Total das contas a pagar: {total}")

