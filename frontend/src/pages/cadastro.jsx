function Cadastro() {
  return (
    <main>
        <header>
            <h1>Cadastro de contas</h1>
        </header>
        <section className="cadastro">
        <h2>Cadastro de contas: </h2>
        <div className="ambiente-cad">
          <form>
            <div className="campo">
              <label htmlFor="nome">Nome da conta</label>
              <input type="text" id="nome" required/>
            </div>
            
            <div className="campo">
              <label htmlFor="dia">Dia do vencimento</label>
              <input type="number" id="dia" required/>
            </div>

            <div className="campo">
              <label htmlFor="mes">Mês do vencimento</label>
              <input type="number" id="mes" required/>
            </div>
            <div className="campo">
              <label htmlFor="valor">Valor da conta</label>
              <input type="number" id="valor" step="0.01" required/>
            </div>

            <div className="campo">
              <label htmlFor="fixa">Essa conta é fixa? </label>
              <input type="checkbox" id="fixa" />
            </div>

            <button type="submit">Cadastrar</button>
          </form>
        </div>
      </section>
    </main>
    
  )
}

export default Cadastro