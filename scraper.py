import requests
from bs4 import BeautifulSoup
from pandas_datareader import data

allowed_symbols = [
    "GOOGL", "GOOG", "MSFT", "CSCO", "AAPL", "NFLX", "FB",
    "ERTS", "ATVI", "SNE",
    "INTL", "ARMH", "QCOM",
    "SNAP", "YEXT", "CLDR", "OKTA", "APPN",
    "QQQ", "GLD",
    "IBM", "HPQ",
    "ZNGA", "BBRY", "YHOO",
    "VMW", "AKAM", "RAX",
    "CHKP", "INTZ", "PANW",
    "V", "FISV", "EBAY",
    "OMISEGo", "Augur", "Filecoin", "Aragon"
]

RANK = 0
COMP = 1
SYMB = 2
WGHT = 3

def write(symbol, weight):
    value_index = 2
    print(symbol, weight, data.get_quote_yahoo(symbol).values[0][value_index])

def main():
    req  = requests.get("https://www.slickcharts.com/sp500")
    soup = BeautifulSoup(req.text, "html.parser")
    tables = soup.find(id="example-1").find("tbody").find_all("tr")
    for table in tables:
        entries = [e for e in list(table.children) if e != "\n"]
        symbol = entries[SYMB].find("input")['value']
        if symbol in allowed_symbols:
            write(symbol, entries[WGHT].string)

if __name__ == "__main__":
    main()
