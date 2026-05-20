import yfinance as yf

class DataFetcher:
    @staticmethod
    def fetch_historical(symbol: str, start: str, end: str):
        '''Fetch OHLC data'''
        df = yf.download(symbol, start=start, end=end, interval='5m')
        return df.dropna()
    
    @staticmethod
    def get_realtime(symbol):
        '''Placeholder for live data'''
        return yf.Ticker(symbol).history(period='1d')