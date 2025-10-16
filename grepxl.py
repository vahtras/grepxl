import sys

import pandas as pd
from rich import print
from rich_tools import df_to_table

def main():
    """
    Display rows of a dataframe from an Excel file that match a given pattern.
    """
    try:
        pattern, xl = sys.argv[1:]
    except ValueError:
        print("Usage: grepxl <pattern> <file>")
        sys.exit(1)
    data = pd.read_excel(xl, engine='calamine').dropna(axis='columns', how='all')
    search = grep(pattern, data)
    print(df_to_table(search, show_index=False))




def grep(pattern:str, data:pd.DataFrame) -> pd.DataFrame:
    """
    Filter rows in a DataFrame that contain the given pattern in any column.
    """
    mask = None
    for col in data.columns:
        update = data[col].astype(str).str.contains(pattern)
        
        if mask is None:
            mask = update
        else:
            mask = mask | update

    return data[mask]


if __name__ == "__main__":
    main()
