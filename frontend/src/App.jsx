import Cadastro from './pages/Cadastro'
import { Routes, Route, useNavigate } from 'react-router-dom'

function App() {
  const navigate = useNavigate()
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
                <div className="coluna-conta">
                  <span className="rotulo">Conta</span>
                  <strong>Internet</strong>
                </div>

                <div className="coluna-conta">
                  <span className="rotulo">Vencimento</span>
                  <span>20/08</span>
                </div>

                <div className="coluna-conta">
                  <span className="rotulo">Valor</span>
                  <strong>R$ 120,00</strong>
                </div>
              </div>
            </section>

            <div className="acao-home">
              <p>Deseja cadastrar uma nova conta?</p>

              <button className="botao-cadastro" type="button"
              onClick={() => navigate('/cadastro')}>
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