
import json
from pathlib import Path


CAMINHO_ARQUIVO = Path(__file__).parent / "contas.json"


# Carrega as contas salvas no arquivo JSON
def carregarContas():

    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            lista_contas = json.load(arquivo)

            if isinstance(lista_contas, list):
                return lista_contas

            return []

    except FileNotFoundError:
        salvarContas([])
        return []

    except json.JSONDecodeError:
        return []


# Salva as contas no arquivo JSON
def salvarContas(lista_contas):

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_contas,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# Cadastra uma nova conta na lista
def cadastrarConta(lista_contas, conta):

    nome = conta["nome"].strip().lower()
    dia = int(conta["dia"])
    mes = int(conta["mes"])
    valor = float(conta["valor"])
    fixa = str(conta["fixa"]).strip().lower()

    # Valida os dados da conta
    if not nome:
        raise ValueError("O nome da conta não pode ficar vazio.")

    if dia < 1 or dia > 31:
        raise ValueError("Dia de vencimento inválido.")

    if mes < 1 or mes > 12:
        raise ValueError("Mês de vencimento inválido.")

    if valor <= 0:
        raise ValueError("O valor da conta deve ser maior que zero.")

    if fixa not in ["sim", "nao"]:
        raise ValueError("Informe sim ou nao para conta fixa.")

    # Cria a conta
    contaAtual = {
        "nome": nome,
        "dia": dia,
        "mes": mes,
        "valor": valor,
        "fixa": fixa
    }

    lista_contas.append(contaAtual)

    return contaAtual


# Calcula o resumo das contas
def resumoContas(contas):

    total = 0
    quantidade = 0
    contaFixa = 0

    for conta in contas:
        quantidade += 1
        total += float(conta["valor"])

        if conta["fixa"] == "sim":
            contaFixa += 1

    return total, quantidade, contaFixa


# Exibe todas as contas cadastradas
def listarContas(contas):

    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return

    print("\n--- CONTAS CADASTRADAS ---")

    for conta in contas:
        print(f"Nome: {conta['nome']}")
        print(f"Vencimento: {conta['dia']}/{conta['mes']}")
        print(f"Valor: R$ {float(conta['valor']):.2f}")
        print(f"Fixa: {conta['fixa']}")
        print("-" * 30)


# Remove uma conta pelo nome
def removeConta(contas, nomeConta):

    nomeConta = nomeConta.strip().lower()

    for conta in contas:
        if conta["nome"].strip().lower() == nomeConta:
            contas.remove(conta)
            return True

    return False
