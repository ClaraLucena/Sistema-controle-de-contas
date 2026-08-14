from fastapi import FastAPI
import contas as contas
from pydantic import BaseModel

class Conta(BaseModel):
    nome: str
    dia: int
    mes: int
    valor: float
    fixa: str

app = FastAPI()

@app.get("/contas")
def buscar_contas():
    return contas.carregarContas()

@app.post("/contas")
def cadastrarContas(lista_contas):
    return contas.cadastrarConta(lista_contas)