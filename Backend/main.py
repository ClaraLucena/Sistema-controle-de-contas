
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal

import contas


# Modelo utilizado no cadastro e na atualização completa
class Conta(BaseModel):
    nome: str
    dia: int = Field(ge=1, le=31)
    mes: int = Field(ge=1, le=12)
    valor: float = Field(gt=0)
    fixa: Literal["sim", "nao"]

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        valor = valor.strip().lower()

        if not valor:
            raise ValueError("O nome da conta não pode ficar vazio.")

        return valor

    @field_validator("fixa")
    @classmethod
    def validar_fixa(cls, valor):
        return valor.strip().lower()


# Modelo utilizado na atualização parcial
class ContaAtualizacao(BaseModel):
    nome: Optional[str] = None
    dia: Optional[int] = Field(default=None, ge=1, le=31)
    mes: Optional[int] = Field(default=None, ge=1, le=12)
    valor: Optional[float] = Field(default=None, gt=0)
    fixa: Optional[Literal["sim", "nao"]] = None

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        if valor is not None:
            valor = valor.strip().lower()

            if not valor:
                raise ValueError("O nome da conta não pode ficar vazio.")

        return valor

    @field_validator("fixa")
    @classmethod
    def validar_fixa(cls, valor):
        if valor is not None:
            return valor.strip().lower()

        return valor


# Criação da aplicação
app = FastAPI()


# Configuração de acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Busca todas as contas
@app.get("/contas")
def buscar_contas():

    return contas.carregarContas()


# Cadastra uma nova conta
@app.post("/contas")
def cadastrar_conta(nova_conta: Conta):

    lista_contas = contas.carregarContas()

    try:
        conta_cadastrada = contas.cadastrarConta(
            lista_contas,
            nova_conta.model_dump()
        )

        contas.salvarContas(lista_contas)

        return {
            "mensagem": "Conta cadastrada com sucesso",
            "conta": conta_cadastrada
        }

    except ValueError as erro:
        raise HTTPException(
            status_code=400,
            detail=str(erro)
        )


# Exclui uma conta pelo nome
@app.delete("/contas/{nomeConta}")
def deletar_conta(nomeConta: str):

    lista_contas = contas.carregarContas()

    removeu = contas.removeConta(lista_contas, nomeConta)

    if not removeu:
        raise HTTPException(
            status_code=404,
            detail="Conta não encontrada"
        )

    contas.salvarContas(lista_contas)

    return {"mensagem": "Conta removida com sucesso"}


# Atualiza todos os dados de uma conta
@app.put("/contas/{nomeConta}")
def atualizar_conta(nomeConta: str, conta_atualizada: Conta):

    lista_contas = contas.carregarContas()

    for conta in lista_contas:

        if conta["nome"].strip().lower() == nomeConta.strip().lower():

            conta.update(conta_atualizada.model_dump())

            contas.salvarContas(lista_contas)

            return {"mensagem": "Conta atualizada com sucesso"}

    raise HTTPException(
        status_code=404,
        detail="Conta não encontrada"
    )


# Atualiza apenas os campos enviados
@app.patch("/contas/{nomeConta}")
def atualizar_parcialmente(nomeConta: str, dados: ContaAtualizacao):

    lista_contas = contas.carregarContas()

    for conta in lista_contas:

        if conta["nome"].strip().lower() == nomeConta.strip().lower():

            dados_atualizados = dados.model_dump(
                exclude_unset=True,
                exclude_none=True
            )

            conta.update(dados_atualizados)

            contas.salvarContas(lista_contas)

            return {"mensagem": "Conta atualizada com sucesso"}

    raise HTTPException(
        status_code=404,
        detail="Conta não encontrada"
    )
