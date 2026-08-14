import contas

#chamada da função que carrega as contas
lista_contas = contas.carregarContas()

# Calcula o resumo das contas que já estavam salvas
total, quantidade, contaFixa = contas.resumoContas(lista_contas)

# Pergunta se o usuário deseja cadastrar uma conta
conta = str.lower(input("Deseja cadastrar uma conta? "))

while conta == "sim":
    contas.cadastrarConta(lista_contas)
    # Atualiza o resumo das contas
    total, quantidade, contaFixa = contas.resumoContas(lista_contas)
    conta = str.lower(input("Deseja cadastrar outra conta? "))

# Exibe todas as contas cadastradas
contas.listarContas(lista_contas)

print(f"Total das contas a pagar: R$ {total:.2f}")

# Pergunta se deseja remover uma conta
remove = str.lower(input("Deseja remover alguma conta? "))

if remove == "sim":
    print("Lista de contas:")

    # Exibe os nomes das contas disponíveis para remoção
    for conta in lista_contas:
        print(conta["nome"])

    removeconta = str.lower(input("Qual conta você deseja remover? "))

    # Chama a função responsável pela remoção
    contas.removeConta(lista_contas, removeconta)

    # Atualiza o resumo depois da remoção
    total, quantidade, contaFixa = contas.resumoContas(lista_contas)


# chama a função para salvar os dados atualizados no JSON
contas.salvarContas(lista_contas)

# Exibe o resumo final
print("\n--- RESUMO ATUALIZADO ---")

contas.listarContas(lista_contas)

print(f"Quantidade de contas: {quantidade}")
print(f"Contas fixas: {contaFixa}")
print(f"Total de contas atualizado: R$ {total:.2f}")