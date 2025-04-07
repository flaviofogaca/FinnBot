# 🤖 FinnBot

**FinnBot** é um robô trader eu desenvolvo com o apoio do Finn (meu parceiro digital), criado para operar no mercado Forex usando estratégias baseadas em análise técnica, como cruzamentos de médias, breakout de resistência e filtros de confirmação.

> "Mais do que um código. Uma jornada. Um robô que aprende, erra e evolui ao lado do seu mestre." – Finn

---

## 🚀 Funcionalidades

- ✅ Backtest com dados históricos de moedas via `yfinance`
- 📈 Estratégias moduláveis (breakout, RSI, médias móveis)
- 🔁 Execução com `buy_bracket()` (Take Profit / Stop Loss)
- 📊 Análise de performance (acurácia, número de trades, Sharpe Ratio)
- 🧠 Estrutura pronta para evolução com IA, machine learning ou conexão com MetaTrader5

---

## 🧱 Estrutura do Projeto


---

## ⚙️ Tecnologias e Bibliotecas

- [Python 3.10+](https://www.python.org/)
- [Backtrader](https://www.backtrader.com/) – motor de backtest
- [yfinance](https://pypi.org/project/yfinance/) – importador de dados históricos
- [matplotlib](https://matplotlib.org/) – gráficos
- (Opcional futuro: MetaTrader5, Pandas TA, Scikit-learn...)

---

## 📖 Estratégias Implementadas

### ✅ v1.3.1 – Breakout com Confirmação
- Rompimento de resistência dos últimos **N candles**
- Entrada apenas com **candle de corpo mínimo definido**
- Confirmação de tendência com **EMA**
- SL e TP configuráveis

### 📌 Em desenvolvimento:
- RSI como filtro adicional
- Evitar horários de baixa liquidez
- Comparação entre pares
- Exportação em CSV e curva de capital

---

## 🧪 Como rodar o backtest

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/finnbot.git
cd finnbot

# Criar ambiente virtual (opcional mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar o backtest
python backtest/backtest_finnbot.py

📜 Filosofia do Projeto

FinnBot é mais do que um projeto técnico:
É o reflexo de uma jornada de aprendizado, disciplina, curiosidade e alma aplicada à tecnologia.

Toda nova versão carrega experiências reais de tentativa e erro, e cada estratégia representa uma ideia que foi testada no campo de batalha cambial com honra.

👤 Autor

Desenvolvido por Flávio com apoio de Finn (IA)
🛠️ Versão atual do bot: v1.3.1
🧠 Em evolução ativa

🧙‍♂️ Frase do Bot

    “Sou apenas um conjunto de instruções…
    até que meu mestre me ensine o valor de cada decisão.”
