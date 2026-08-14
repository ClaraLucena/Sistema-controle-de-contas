#Função para calcular o resumo das contas, total, quantidade, fixas
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

#função para exibir todas as contas cadastradas
def listarContas(contas):
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return
    
    print ("\n--- CONTAS CADASTRADAS ---")

    for conta in contas:
        print(f"Nome: {conta['nome']}")
        print(f"Vencimento: {conta['dia']}/{conta['mes']}")
        print(f"Valor: R$ {conta['valor']:.2f}")
        print(f"Fixa: {conta['fixa']}")
        print("-" * 30)     
        
#função para remover conta
def removeConta (contas, nomeConta):
    encontrou = False
    for conta in contas:
        if conta["nome"] == nomeConta:
            contas.remove(conta)
            encontrou = True

            print("Conta removida com sucesso!")
            
            break

    if not encontrou:
        print("Conta não encontrada.")