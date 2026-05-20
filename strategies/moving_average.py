import pandas as pd

class MovingAverageStrategy:
    def generate_signal(self, data: pd.DataFrame) -> str:
        if len(data) < 50:
            return 'hold'
        data['SMA_short'] = data['Close'].rolling(window=20).mean()
        data['SMA_long'] = data['Close'].rolling(window=50).mean()
        
        latest = data.iloc[-1]
        prev = data.iloc[-2]
        
        if prev['SMA_short'] <= prev['SMA_long'] and latest['SMA_short'] > latest['SMA_long']:
            return 'buy'
        elif prev['SMA_short'] >= prev['SMA_long'] and latest['SMA_short'] < latest['SMA_long']:
            return 'sell'
        return 'hold'