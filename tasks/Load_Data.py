import polars as pl
import os

def save_polars_to_csv(pl_data:pl.DataFrame, file_path):
    """
    Saves a Polars DataFrame to a CSV file.

    Parameters:
    - pl_data (pl.DataFrame): The Polars DataFrame to save.
    - file_path (str): The path where the CSV file will be saved, including the file name.

    Returns:
    - None
    """
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_path = file_path + "/{ticker_}_stock_prices.parquet"
        if not os.path.exists(file_path):
            pl_data.write_parquet(file_path)
            print(f"Polars DataFrame successfully saved to {file_path}")
            return True
        else:
            existing_data = pl.read_parquet(file_path)
            new_data = existing_data.vstack(pl_data)
            new_data.write_parquet(file_path)
    except Exception as e:
        print(f"An error occurred while saving the DataFrame to CSV: {e}")
        return False