import polars as pl

def process_yfinance_data(data, ticker):
    """
    Processes Yahoo Finance data by resetting the index, converting it to a Polars DataFrame,
    and renaming columns for clarity.

    Parameters:
    - data (pandas.DataFrame): The data fetched from Yahoo Finance.
    - ticker (str): The ticker symbol for the data, used in column renaming.

    Returns:
    - pl.DataFrame: A Polars DataFrame with renamed columns.
    """
    data.reset_index(inplace=True)
    pl_data = pl.from_pandas(data)
    return pl_data.rename({
        f"('Adj Close', '{ticker}')": f'{ticker}_Adj_Close',
        f"('Close', '{ticker}')": f'{ticker}_Close',
        f"('High', '{ticker}')": f'{ticker}_High',
        f"('Low', '{ticker}')": f'{ticker}_Low',
        f"('Open', '{ticker}')": f'{ticker}_Open',
        f"('Volume', '{ticker}')": f'{ticker}_Volume',
        f"('Date', '')": 'Date'
    })
