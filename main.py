import json


def resumoContas (contas):
    total = 0
    quantidade = 0
    contaFixa = 0
    for conta in contas:
        quantidade += 1
        total += conta["valor"]

        if conta["fixa"] == "sim":
            contaFixa += 1
    return total, quantidade, contaFixa

#salva os arquivos sem apagar os anteriores:
try:
    with open("contas.json", "r") as conta:
        contas = json.load(conta)
except:
    contas = []

# Percorre as contas carregadas do JSON para atualizar quantidade, total e contas fixas


conta = str.lower(input("Deseja cadastrar a conta? "))

while conta == "sim":
    nome = str.lower(input("Nome da conta: "))
    data = int(input("Informe a dia do vencimento: "))
    mes = int(input("Informe o mês do vencimento: "))
    valor = float(input("Valor da conta: "))

    if ((data >=1 and data <=31) and (mes >=1 and mes<=12)):
        print("data valida")
        fixa = str.lower(input("esta conta é fixa? "))

        contaAtual={
            "nome": nome,
             "dia": data,
             "mes": mes,
             "valor": valor,
            "fixa": fixa
        }
        #adiciona os dados na array  
        contas.append(contaAtual)
        total, quantidade, contaFixa = resumoContas(contas)

    else: 
        print("data inválida")
    conta = str.lower(input("Deseja cadastrar outra conta? "))



#percorre as informações das contas e exibe
for conta in contas:
    print(f"Nome: {conta['nome']}")
    print(f"Vencimento: {conta['dia']}/{conta['mes']}")
    print(f"Valor: R$ {conta['valor']:.2f}")
    print(f"Fixa: {conta['fixa']}")
    print("-" * 30)

print(f"Total das contas a pagar: R${total:.2f}")

remove = str.lower(input("Deseja remover alguma conta? "))

if remove == "sim":
    print("lista de contas: ")
    #percorre a lsita para ver qual remover
    for conta in contas:
        print(conta['nome'])
    removeconta= str.lower(input("Qual conta você deseja remover? "))
    

#percorre as contas para remover
    encontrou = False

    for conta in contas:
        if conta["nome"] == removeconta:
            contas.remove(conta)
            encontrou = True
            print("Conta removida com sucesso!")
            
            break

    if not encontrou:
        print("Conta não encontrada.")

    total, quantidade, contaFixa = resumoContas(contas)
#salva os dados novos no json
with open("contas.json", "w") as conta:
    json.dump(contas, conta, indent=4)


print("\nResumo atualizado")
print(f"Quantidade de contas: {quantidade}")
print(f"Contas fixas: {contaFixa}")    
print(f"Total de contas atualizado: R${total:.2f} ")