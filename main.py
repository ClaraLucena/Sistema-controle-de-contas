import json
import contas


# Carrega as contas salvas sem apagar as anteriores
try:
    with open("contas.json", "r") as arquivo:
        lista_contas = json.load(arquivo)

except:
    lista_contas = []


# Calcula o resumo das contas que já estavam salvas
total, quantidade, contaFixa = contas.resumoContas(lista_contas)


# Pergunta se o usuário deseja cadastrar uma conta
conta = input("Deseja cadastrar uma conta? ").lower()


while conta == "sim":

    nome = input("Nome da conta: ").lower()
    data = int(input("Informe o dia do vencimento: "))
    mes = int(input("Informe o mês do vencimento: "))
    valor = float(input("Valor da conta: "))


    # Verifica se a data é válida
    if ((data >= 1 and data <= 31) and
        (mes >= 1 and mes <= 12)):

        print("Data válida.")

        fixa = input("Esta conta é fixa? (sim / nao): ").lower()


        # Valida a resposta sobre conta fixa
        while fixa != "sim" and fixa != "nao":

            print("Digite apenas sim ou nao.")

            fixa = input(
                "Esta conta é fixa? (sim / nao): "
            ).lower()


        # Cria a conta atual
        contaAtual = {
            "nome": nome,
            "dia": data,
            "mes": mes,
            "valor": valor,
            "fixa": fixa
        }


        # Adiciona a nova conta à lista
        lista_contas.append(contaAtual)


        # Atualiza o resumo das contas
        total, quantidade, contaFixa = contas.resumoContas(
            lista_contas
        )


    else:
        print("Data inválida.")


    conta = input(
        "Deseja cadastrar outra conta? "
    ).lower()


# Exibe todas as contas cadastradas
contas.listarContas(lista_contas)

print(f"Total das contas a pagar: R$ {total:.2f}")


# Pergunta se deseja remover uma conta
remove = input(
    "Deseja remover alguma conta? "
).lower()


if remove == "sim":

    print("Lista de contas:")


    # Exibe os nomes das contas disponíveis para remoção
    for conta in lista_contas:
        print(conta["nome"])


    removeconta = input(
        "Qual conta você deseja remover? "
    ).lower()


    # Chama a função responsável pela remoção
    contas.removeConta(
        lista_contas,
        removeconta
    )


    # Atualiza o resumo depois da remoção
    total, quantidade, contaFixa = contas.resumoContas(
        lista_contas
    )


# Salva os dados atualizados no JSON
with open("contas.json", "w") as arquivo:

    json.dump(
        lista_contas,
        arquivo,
        indent=4
    )


# Exibe o resumo final
print("\n--- RESUMO ATUALIZADO ---")

contas.listarContas(lista_contas)

print(f"Quantidade de contas: {quantidade}")
print(f"Contas fixas: {contaFixa}")
print(f"Total de contas atualizado: R$ {total:.2f}")