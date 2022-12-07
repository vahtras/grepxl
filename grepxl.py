import sys
import warnings

import pandas as pd
from rich import print
from rich_tools import df_to_table


def grep(pattern, data):
    mask = None
    for col in data.columns:
        if data[col].dtype != object:
            continue
        if mask is None:
            mask = data[col].str.contains(pattern)
        else:
            mask = mask | data[col].str.contains(pattern)

    return data[mask]


def main():
    pattern, xl = sys.argv[1:]
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        data = pd.read_excel(xl, engine='openpyxl')
    search = grep(pattern, data)
    print(df_to_table(search, show_index=False))


if __name__ == "__main__":
    main()
