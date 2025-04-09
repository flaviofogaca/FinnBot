import backtrader as bt
import yfinance as yf
import pandas as pd
import os
import sys

# Corrige caminho para importar estratégia
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from strategies.finnbot_crypto import FinnBotCrypto

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(FinnBotCrypto)

    df = yf.download('BTC-USD', start='2025-02-10', end='2025-04-07', interval='15m', auto_adjust=False, group_by='ticker')


    if df.empty:
        print("❌ Nenhum dado foi carregado do Yahoo Finance. Verifique o intervalo ou o símbolo.")
        exit()

    # Agora pegamos só o DataFrame interno do ticker
    df = df['BTC-USD']
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)

    data = bt.feeds.PandasData(dataname=df)

    cerebro.adddata(data)
    cerebro.broker.set_cash(10000)
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="sharpe")
    results = cerebro.run()
    strat = results[0]

    print("\n📊 [RESULTADOS DO BACKTEST]")

    # TradeAnalyzer
    ta = strat.analyzers.ta.get_analysis()

    total_trades = ta.get('total', {}).get('closed', 0)
    won_trades = ta.get('won', {}).get('total', 0)
    lost_trades = ta.get('lost', {}).get('total', 0)

    print("🔹 Total de trades:", total_trades)
    print("🔹 Ganhos:", won_trades)
    print("🔹 Perdas:", lost_trades)

    if total_trades > 0:
        win_rate = (won_trades / total_trades) * 100
        print(f"🔹 % de acerto: {win_rate:.2f}%")
    else:
        print("🔹 % de acerto: 0%")

    # Sharpe Ratio
    sharpe = strat.analyzers.sharpe.get_analysis()
    print("📈 Sharpe Ratio:", sharpe.get('sharperatio', 'N/A'))

    cerebro.plot()
