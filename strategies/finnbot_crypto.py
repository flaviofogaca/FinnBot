import backtrader as bt

class FinnBotCrypto(bt.Strategy):
    params = (
        ('resistance_lookback', 15),
        ('ema_period', 20),
        ('min_candle_body_pct', 0.003),  # 1.5%
        ('stop_loss_pct', 0.015),         # 2%
        ('take_profit_pct', 0.015),       # 1%
    )

    def __init__(self):
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.ema_period)
        self.order = None

    def log(self, txt):
        dt = self.datas[0].datetime.datetime(0)
        print(f'{dt.isoformat()}, {txt}')

    def next(self):
        if self.order:
            return

        if len(self.data) < self.params.resistance_lookback + 1:
            return

        if not self.position:
            resistance = max(self.data.high.get(size=self.params.resistance_lookback)[0:-1])
            candle_body = self.data.close[0] - self.data.open[0]
            candle_body_pct = candle_body / self.data.open[0]

            if (
                self.data.close[0] > resistance and
                candle_body > 0 and
                candle_body_pct > self.params.min_candle_body_pct and
                self.data.close[0] > self.ema[0]
            ):
                self.log(f'💥 CRIPTO BREAKOUT BUY @ {self.data.close[0]:.2f} | Res: {resistance:.2f}')

                sl_price = self.data.close[0] - self.data.close[0] * self.params.stop_loss_pct
                tp_price = self.data.close[0] + self.data.close[0] * self.params.take_profit_pct

                self.order = self.buy_bracket(
                    price=self.data.close[0],
                    stopprice=sl_price,
                    limitprice=tp_price
                )

    def notify_order(self, order):
        if order.status in [order.Completed, order.Canceled, order.Margin]:
            self.order = None
