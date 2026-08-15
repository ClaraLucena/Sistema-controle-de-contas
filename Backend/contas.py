import json
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "contas.json"
def carregarContas():
    # Carrega as contas salvas sem apagar as anteriores
    try:
        with open(CAMINHO_ARQUIVO, "r") as arquivo:
            lista_contas = json.load(arquivo)

    except:
        lista_contas = []
    return lista_contas

#Função para cadastrar as contas
def cadastrarConta (lista_contas):
    
    nome = input("Nome da conta: ").lower()
    data = int(input("Informe o dia do vencimento: "))
    mes = int(input("Informe o mês do vencimento: "))
    valor = float(input("Valor da conta: "))


    # Verifica se a data é válida
    if ((data >= 1 and data <= 31) and
        (mes >= 1 and mes <= 12)):

        print("Data válida.")

        fixa = str.lower(input("Esta conta é fixa? (sim / nao): "))


        # Valida a resposta sobre conta fixa
        while fixa != "sim" and fixa != "nao":

            print("Digite apenas sim ou nao.")

            fixa = str.lower(input("Esta conta é fixa? (sim / nao): "))


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


    else:
        print("Data inválida.")
    
        
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

def salvarContas (lista_contas):
    with open(CAMINHO_ARQUIVO, "w") as arquivo:
        json.dump(lista_contas, arquivo, indent=4)
    
#função para remover conta
def removeConta(contas, nomeConta):
    nomeConta = nomeConta.strip().lower()

    for conta in contas:
        if conta["nome"].strip().lower() == nomeConta:
            contas.remove(conta)
            return True

    return False
