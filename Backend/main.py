from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import contas


class Conta(BaseModel):
    nome: str
    dia: int
    mes: int
    valor: float
    fixa: str


class ContaAtualizacao(BaseModel):
    nome: Optional[str] = None
    dia: Optional[int] = None
    mes: Optional[int] = None
    valor: Optional[float] = None
    fixa: Optional[str] = None


app = FastAPI()


@app.get("/contas")
def buscar_contas():
    return contas.carregarContas()


@app.post("/contas")
def cadastrar_conta(nova_conta: Conta):
    lista_contas = contas.carregarContas()

    lista_contas.append(nova_conta.model_dump())

    contas.salvarContas(lista_contas)

    return {"mensagem": "Conta cadastrada com sucesso"}


@app.delete("/contas/{nomeConta}")
def deletar_conta(nomeConta: str):
    lista_contas = contas.carregarContas()

    removeu = contas.removeConta(lista_contas, nomeConta)

    if removeu:
        contas.salvarContas(lista_contas)
        return {"mensagem": "Conta removida com sucesso"}

    return {"mensagem": "Conta não encontrada"}


@app.put("/contas/{nomeConta}")
def atualizar_conta(nomeConta: str, conta_atualizada: Conta):
    lista_contas = contas.carregarContas()

    for conta in lista_contas:
        if conta["nome"] == nomeConta:

            conta["nome"] = conta_atualizada.nome
            conta["dia"] = conta_atualizada.dia
            conta["mes"] = conta_atualizada.mes
            conta["valor"] = conta_atualizada.valor
            conta["fixa"] = conta_atualizada.fixa

            contas.salvarContas(lista_contas)

            return {"mensagem": "Conta atualizada com sucesso"}

    return {"mensagem": "Conta não encontrada"}


@app.patch("/contas/{nomeConta}")
def atualizar_parcialmente(nomeConta: str, dados: ContaAtualizacao):
    lista_contas = contas.carregarContas()

    for conta in lista_contas:
        if conta["nome"] == nomeConta:

            dados_atualizados = dados.model_dump(exclude_unset=True)

            for campo, valor in dados_atualizados.items():
                conta[campo] = valor

            contas.salvarContas(lista_contas)

            return {"mensagem": "Conta atualizada com sucesso"}

    return {"mensagem": "Conta não encontrada"}