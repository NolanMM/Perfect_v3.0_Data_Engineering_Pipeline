from tasks.Retrieve_Data import fetch_dow_jones_data
from tasks.Processing_Data import process_yfinance_data
from tasks.Load_Data import save_polars_to_csv
from prefect import task, flow
from datetime import timedelta

TICKER = '^DJI'

@task
def retrieve_raw_data(ticker_=TICKER):
    df_stock_prices_ = fetch_dow_jones_data(ticker_)
    return df_stock_prices_, ticker_

@task
def process_data(df_stock_prices_, ticker_):
    df_stock_prices_processed_ = process_yfinance_data(df_stock_prices_, ticker_)
    return df_stock_prices_processed_

@task
def save_data_to_csv(df_stock_prices_, ticker_):
    filepath = f'./data_storage/{ticker_}'
    return save_polars_to_csv(df_stock_prices_, filepath)

@flow(log_prints=True)
def data_retrieve_pipeline_flow():
    df_stock_prices, ticker = retrieve_raw_data()
    df_stock_prices_processed_ = process_data(df_stock_prices, ticker)
    result = save_data_to_csv(df_stock_prices_processed_, ticker)
    if result:
        print("Data Pipeline Completed Successfully")
    else:
        print("Data Pipeline Failed")

if __name__ == "__main__":
    data_retrieve_pipeline_flow.serve(
        name="simple-data-engineering-pipeline-flow",
        interval=timedelta(minutes=1)
    )