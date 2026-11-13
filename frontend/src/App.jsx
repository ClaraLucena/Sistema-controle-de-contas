
import { useState, useEffect } from 'react'
import Cadastro from './pages/cadastro'
import { Routes, Route, useNavigate } from 'react-router-dom'

function App() {
  const navigate = useNavigate()

  const [contas, setContas] = useState([])
  const [contaEditando, setContaEditando] = useState(null)

  // Busca as contas no backend
  async function buscarContas() {
    try {
      const resposta = await fetch('http://127.0.0.1:8000/contas')

      if (!resposta.ok) {
        throw new Error('Erro ao buscar contas')
      }

      const dados = await resposta.json()
      setContas(dados)

    } catch (erro) {
      console.error('Erro:', erro)
    }
  }

  useEffect(() => {
    buscarContas()
  }, [])

  // Exclui uma conta
  async function excluirConta(nomeConta) {
    const confirmar = window.confirm(
      `Tem certeza que deseja excluir a conta ${nomeConta}?`
    )

    if (!confirmar) {
      return
    }

    try {
      const resposta = await fetch(
        `http://127.0.0.1:8000/contas/${encodeURIComponent(nomeConta)}`,
        {
          method: 'DELETE'
        }
      )

      const dados = await resposta.json()

      if (!resposta.ok || dados.mensagem === 'Conta não encontrada') {
        alert('Não foi possível excluir a conta.')
        return
      }

      alert('Conta excluída com sucesso!')
      await buscarContas()

    } catch (erro) {
      console.error('Erro:', erro)
      alert('Não foi possível conectar ao servidor.')
    }
  }

  // Seleciona uma conta para editar
  function editarConta(conta) {
    setContaEditando({
      nomeOriginal: conta.nome,
      nome: conta.nome,
      dia: conta.dia,
      mes: conta.mes,
      valor: conta.valor,
      fixa: conta.fixa
    })
  }

  // Atualiza os dados da conta
  async function salvarEdicao(e) {
    e.preventDefault()

    const contaAtualizada = {
      nome: contaEditando.nome,
      dia: Number(contaEditando.dia),
      mes: Number(contaEditando.mes),
      valor: Number(contaEditando.valor),
      fixa: contaEditando.fixa
    }

    try {
      const resposta = await fetch(
        `http://127.0.0.1:8000/contas/${encodeURIComponent(contaEditando.nomeOriginal)}`,
        {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(contaAtualizada)
        }
      )

      const dados = await resposta.json()

      if (!resposta.ok || dados.mensagem === 'Conta não encontrada') {
        alert('Não foi possível atualizar a conta.')
        return
      }

      alert('Conta atualizada com sucesso!')

      setContaEditando(null)
      await buscarContas()

    } catch (erro) {
      console.error('Erro:', erro)
      alert('Não foi possível conectar ao servidor.')
    }
  }

  // Calcula o total das contas
  const total = contas.reduce((soma, conta) => {
    return soma + Number(conta.valor)
  }, 0)

  // Conta as contas fixas
  const quantidadeFixas = contas.filter(
    conta => conta.fixa === 'sim'
  ).length

  return (
    <Routes>
      <Route
        path="/"
        element={
          <main className="pagina-principal">
            <header>
              <h1>Controle de Contas</h1>
              <p>Organize suas contas de forma simples e prática.</p>
            </header>

            <section className="resumo">
              <div className="card">
                <p>Total a pagar</p>
                <h2>
                  {total.toLocaleString('pt-BR', {
                    style: 'currency',
                    currency: 'BRL'
                  })}
                </h2>
              </div>

              <div className="card">
                <p>Quantidade de contas</p>
                <h2>{contas.length}</h2>
              </div>

              <div className="card">
                <p>Contas fixas</p>
                <h2>{quantidadeFixas}</h2>
              </div>
            </section>

            <section className="proximas">
              <h2>Contas cadastradas</h2>

              {contas.length === 0 ? (
                <p>Nenhuma conta cadastrada.</p>
              ) : (
                contas.map((conta, indice) => (
                  <div className="conta-proxima" key={indice}>
                    <div className="coluna-conta">
                      <span className="rotulo">Conta</span>
                      <strong>{conta.nome}</strong>
                    </div>

                    <div className="coluna-conta">
                      <span className="rotulo">Vencimento</span>
                      <span>{conta.dia}/{conta.mes}</span>
                    </div>

                    <div className="coluna-conta">
                      <span className="rotulo">Valor</span>
                      <strong>
                        {Number(conta.valor).toLocaleString('pt-BR', {
                          style: 'currency',
                          currency: 'BRL'
                        })}
                      </strong>
                    </div>

                    <div className="coluna-acoes">
                      <button
                        className="botao-editar"
                        type="button"
                        onClick={() => editarConta(conta)}
                      >
                        Editar
                      </button>

                      <button
                        className="botao-excluir"
                        type="button"
                        onClick={() => excluirConta(conta.nome)}
                      >
                        Excluir
                      </button>
                    </div>
                  </div>
                ))
              )}
            </section>

            {/* Formulário de edição */}
            {contaEditando && (
              <section className="formulario-edicao">
                <h2>Editar conta</h2>

                <form onSubmit={salvarEdicao}>
                  <div className="campo">
                    <label htmlFor="editar-nome">Nome da conta</label>
                    <input
                      id="editar-nome"
                      type="text"
                      value={contaEditando.nome}
                      onChange={(e) =>
                        setContaEditando({
                          ...contaEditando,
                          nome: e.target.value
                        })
                      }
                      required
                    />
                  </div>

                  <div className="campo">
                    <label htmlFor="editar-dia">Dia do vencimento</label>
                    <input
                      id="editar-dia"
                      type="number"
                      min="1"
                      max="31"
                      value={contaEditando.dia}
                      onChange={(e) =>
                        setContaEditando({
                          ...contaEditando,
                          dia: e.target.value
                        })
                      }
                      required
                    />
                  </div>

                  <div className="campo">
                    <label htmlFor="editar-mes">Mês do vencimento</label>
                    <input
                      id="editar-mes"
                      type="number"
                      min="1"
                      max="12"
                      value={contaEditando.mes}
                      onChange={(e) =>
                        setContaEditando({
                          ...contaEditando,
                          mes: e.target.value
                        })
                      }
                      required
                    />
                  </div>

                  <div className="campo">
                    <label htmlFor="editar-valor">Valor da conta</label>
                    <input
                      id="editar-valor"
                      type="number"
                      min="0.01"
                      step="0.01"
                      value={contaEditando.valor}
                      onChange={(e) =>
                        setContaEditando({
                          ...contaEditando,
                          valor: e.target.value
                        })
                      }
                      required
                    />
                  </div>

                  <div className="campo">
                    <label htmlFor="editar-fixa">Essa conta é fixa?</label>
                    <input
                      id="editar-fixa"
                      type="checkbox"
                      checked={contaEditando.fixa === 'sim'}
                      onChange={(e) =>
                        setContaEditando({
                          ...contaEditando,
                          fixa: e.target.checked ? 'sim' : 'nao'
                        })
                      }
                    />
                  </div>

                  <div className="acoes-edicao">
                    <button type="submit">
                      Salvar alterações
                    </button>

                    <button
                      type="button"
                      className="botao-cancelar"
                      onClick={() => setContaEditando(null)}
                    >
                      Cancelar
                    </button>
                  </div>
                </form>
              </section>
            )}

            <div className="acao-home">
              <p>Deseja cadastrar uma nova conta?</p>

              <button
                className="botao-cadastro"
                type="button"
                onClick={() => navigate('/cadastro')}
              >
                Cadastrar nova conta
              </button>
            </div>
          </main>
        }
      />

      <Route
        path="/cadastro"
        element={<Cadastro />}
      />
    </Routes>
  )
}

export default App
