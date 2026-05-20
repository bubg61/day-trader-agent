class RiskManager:
    def __init__(self, risk_per_trade=0.01):
        self.risk_per_trade = risk_per_trade
    
    def assess_trade(self, data, signal):
        '''Basic risk check'''
        return True  # Expand with stop loss, volatility etc.
    
    def calculate_size(self, capital, price):
        return int((capital * self.risk_per_trade) / (price * 0.02))  # Example