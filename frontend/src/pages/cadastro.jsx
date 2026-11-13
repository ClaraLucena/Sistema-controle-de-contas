
import { useState, useEffect } from 'react'

function Cadastro() {
  const [nome, setNome] = useState('')
  const [dia, setDia] = useState('')
  const [mes, setMes] = useState('')
  const [valor, setValor] = useState('')
  const [fixa, setFixa] = useState(false)

  const [contas, setContas] = useState([])

  // Busca as contas cadastradas quando a página é carregada
  useEffect(() => {
    async function buscarContas() {
      try {
        const resposta = await fetch('http://127.0.0.1:8000/contas')

        if (!resposta.ok) {
          throw new Error('Erro ao buscar contas')
        }

        const dados = await resposta.json()
        setContas(dados)
      } catch (erro) {
        console.error(erro)
        alert('Não foi possível carregar as contas.')
      }
    }

    buscarContas()
  }, [])

  // Cadastra uma nova conta
  async function cadastrarConta(e) {
    e.preventDefault()

    const novaConta = {
      nome: nome,
      dia: Number(dia),
      mes: Number(mes),
      valor: Number(valor),
      fixa: fixa ? 'sim' : 'nao'
    }

    try {
      const resposta = await fetch('http://127.0.0.1:8000/contas', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(novaConta)
      })

      if (!resposta.ok) {
        alert('Erro ao cadastrar conta!')
        return
      }

      const dados = await resposta.json()

      // Atualiza a lista sem precisar recarregar a página
      setContas(contasAtuais => [...contasAtuais, novaConta])

      alert(dados.mensagem || 'Conta cadastrada com sucesso!')

      // Limpa os campos
      setNome('')
      setDia('')
      setMes('')
      setValor('')
      setFixa(false)

    } catch (erro) {
      console.error(erro)
      alert('Não foi possível conectar ao servidor.')
    }
  }

  return (
    <main className="pagina-cadastro">
      <section className="cadastro">
        <h1>Cadastro de contas</h1>

        <div className="ambiente-cad">
          <form onSubmit={cadastrarConta}>

            <div className="campo">
              <label htmlFor="nome">Nome da conta</label>
              <input
                type="text"
                id="nome"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                required
              />
            </div>

            <div className="campo">
              <label htmlFor="dia">Dia do vencimento</label>
              <input
                type="number"
                id="dia"
                min="1"
                max="31"
                value={dia}
                onChange={(e) => setDia(e.target.value)}
                required
              />
            </div>

            <div className="campo">
              <label htmlFor="mes">Mês do vencimento</label>
              <input
                type="number"
                id="mes"
                min="1"
                max="12"
                value={mes}
                onChange={(e) => setMes(e.target.value)}
                required
              />
            </div>

            <div className="campo">
              <label htmlFor="valor">Valor da conta</label>
              <input
                type="number"
                id="valor"
                min="0.01"
                step="0.01"
                value={valor}
                onChange={(e) => setValor(e.target.value)}
                required
              />
            </div>

            <div className="campo">
              <label htmlFor="fixa">Essa conta é fixa?</label>
              <input
                type="checkbox"
                id="fixa"
                checked={fixa}
                onChange={(e) => setFixa(e.target.checked)}
              />
            </div>

            <button type="submit">Cadastrar</button>
          </form>
        </div>
      </section>

      {/* Lista de contas cadastradas */}
      <section className="lista-contas">
        <h2>Contas cadastradas</h2>

        {contas.length === 0 ? (
          <p>Nenhuma conta cadastrada.</p>
        ) : (
          contas.map((conta, indice) => (
            <div className="item-conta" key={indice}>
              <h3>{conta.nome}</h3>

              <p>
                Vencimento: {conta.dia}/{conta.mes}
              </p>

              <p>
                Valor: R$ {Number(conta.valor).toFixed(2)}
              </p>

              <p>
                Conta fixa: {conta.fixa}
              </p>
            </div>
          ))
        )}
      </section>
    </main>
  )
}

export default Cadastro
