import pandas as pd
import numpy as np

# sys.path.insert(1, 
from utility import util_example

def read_data(path):
    data = pd.read_csv(path)
    return data

def main():
    # util_example.purpose()
    util_example.info()


if __name__ == '__main__':
    main()
