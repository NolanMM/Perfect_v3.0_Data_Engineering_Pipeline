from datetime import datetime
import yfinance as yf
import polars as pl

def fetch_dow_jones_data(ticker='^DJI', start_date='2000-01-01', end_date=None):
    """
    Fetches historical data for the Dow Jones Industrial Average from Yahoo Finance,
    processes it into a Polars DataFrame, and renames columns for easier use.

    Parameters:
    - ticker (str): The ticker symbol for the desired stock/index. Default is '^DJI'.
    - start_date (str): The start date for the data in 'YYYY-MM-DD' format. Default is '2000-01-01'.
    - end_date (str): The end date for the data in 'YYYY-MM-DD' format. Default is today's date.

    Returns:
    - pl.DataFrame: A Polars DataFrame containing the processed historical data.
    """
    if end_date is None: end_date = datetime.today().strftime('%Y-%m-%d')
    return yf.download(ticker, start=start_date, end=end_date)