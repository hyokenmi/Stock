import pandas as pd

def get_max_close(symbol):
    """ Return the maximum closing value for stock indicted by symbol.
    Note: data for a stock is store in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df.head() #print entire dataframe

    for symbol in ['AAPL', 'IBM']:
        print "Max close"
        print symbol, get_max_close(symbol)

if __name__ == "__main__":
    test_run()
