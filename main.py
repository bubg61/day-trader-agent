from data.fetcher import DataFetcher
from agents.trading_agent import TradingAgent
from strategies.moving_average import MovingAverageStrategy
from risk.manager import RiskManager
from backtest.engine import BacktestEngine

def main():
    print('🚀 Starting Day Trader Agent...')
    fetcher = DataFetcher()
    strategy = MovingAverageStrategy()
    risk_manager = RiskManager()
    agent = TradingAgent(strategy, risk_manager)
    
    # Example backtest
    engine = BacktestEngine()
    data = fetcher.fetch_historical('AAPL', '2025-01-01', '2025-05-01')
    results = engine.run(data, agent)
    print('Backtest Results:', results)

if __name__ == "__main__":
    main()