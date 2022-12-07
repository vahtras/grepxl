import sys
import pandas as pd


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
    data = pd.read_excel(xl, engine='openpyxl')
    search = grep(pattern, data)
    print(search)


if __name__ == "__main__":
    main()
