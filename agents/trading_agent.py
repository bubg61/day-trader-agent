class TradingAgent:
    def __init__(self, strategy, risk_manager):
        self.strategy = strategy
        self.risk_manager = risk_manager
    
    def get_decision(self, market_data):
        signal = self.strategy.generate_signal(market_data)
        risk_ok = self.risk_manager.assess_trade(market_data, signal)
        if signal == 'buy' and risk_ok:
            return 'BUY'
        elif signal == 'sell':
            return 'SELL'
        return 'HOLD'