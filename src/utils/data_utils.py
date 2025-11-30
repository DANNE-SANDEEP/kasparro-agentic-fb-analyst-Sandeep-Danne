import pandas as pd
from src.utils.logging_utils import log_info, log_error

def load_csv_data(file_path):
    """
    Loads CSV file and returns a cleaned pandas DataFrame.
    - Converts Date column to datetime
    - Strips column names
    """
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()

        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        log_info(f"Loaded: {file_path} | Rows: {len(df)} | Columns: {list(df.columns)}")
        return df

    except FileNotFoundError:
        log_error(f"❌ File not found: {file_path}")
        return pd.DataFrame()

    except Exception as e:
        log_error(f"❌ Error loading CSV: {str(e)}")
        return pd.DataFrame()