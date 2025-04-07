import backtrader as bt

class FinnBotStrategy(bt.Strategy):
    params = (
        ('resistance_lookback', 50),
        ('ema_period', 20),
        ('min_candle_body', 0.0010),  # corpo mínimo de 5 pips
        ('stop_loss', 20),
        ('take_profit', 10),
    )

    def __init__(self):
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.ema_period)
        self.order = None

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')

    def next(self):
        if self.order:
            return

        if len(self.data) < self.params.resistance_lookback + 1:
            return

        if not self.position:
            # Define resistência
            resistance = max(self.data.high.get(size=self.params.resistance_lookback)[0:-1])

            candle_body = self.data.close[0] - self.data.open[0]

            if (
                self.data.close[0] > resistance and                      # Rompeu resistência
                candle_body > self.params.min_candle_body and           # Candle de força
                self.data.close[0] > self.ema[0]                        # Acima da EMA (tendência de alta)
            ):
                self.log(f'BREAKOUT CONFIRMADO: BUY @ {self.data.close[0]:.5f} | Res: {resistance:.5f}')
                self.order = self.buy_bracket(
                    price=self.data.close[0],
                    stopprice=self.data.close[0] - self.params.stop_loss * 0.0001,
                    limitprice=self.data.close[0] + self.params.take_profit * 0.0001
                )

    def notify_order(self, order):
        if order.status in [order.Completed, order.Canceled, order.Margin]:
            self.order = None
