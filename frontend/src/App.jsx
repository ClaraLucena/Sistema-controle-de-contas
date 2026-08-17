function App() {
  return (
    <main>
      <header>
        <h1>Controle de Contas</h1>
        <p>Organize suas contas de forma simples e prática.</p>
      </header>

      <section className="resumo">
        <div className="card">
          <p>Total a pagar</p>
          <h2>R$ 0,00</h2>
        </div>

        <div className="card">
          <p>Quantidade de contas</p>
          <h2>0</h2>
        </div>

        <div className="card">
          <p>Contas fixas</p>
          <h2>0</h2>
        </div>
      </section>

      <section className="proximas">
        <h2>Próximas contas a vencer</h2>
        <div className="conta-proxima">
          <span>Internet</span>
          <span>Vence dia 20</span>
          <strong>R$ 120,00</strong>
        </div>
      </section>

      <button type="button">
        Cadastrar nova conta
      </button>
    </main>
  )
}

export default App