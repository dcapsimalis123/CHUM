import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse as arg
import sys, os

sys.path.insert(0, "C:\\Users\\Donovan\\Desktop\\CHUM\\")
from usefulFuncs import check_float

# arguments
arg_parser = arg.ArgumentParser()
arg_parser.add_argument('-f1', '--file1')
arg_parser.add_argument('-f2', '--file2')
arg_parser.add_argument('-a', '--Absolute')
arg_parser.add_argument('-p', '--Percent')
arg_parser.add_argument('-c', '--Columns', default=None, type=lambda x: x or None)
arg = arg_parser.parse_args()

# Load data sets
data_set1 = np.array(pd.read_csv(arg.file1))
data_set2 = np.array(pd.read_csv(arg.file2))

# check files are valid shape for comparison
if np.shape(data_set1) != np.shape(data_set2):
    if len(sys.argv) <= 4:
        print('Data Sets of differing shape')
        quit()

# calc the basic amount of all diffs for either all columns or a selection of columns
print(arg.Columns)
if not arg.Columns:
    cols = range(data_set1.shape[0])
else:
    cols = arg.Columns.split(',')
    cols = [int(c) for c in cols]

diffs = np.array([data_set1[i] - data_set2[i] for i in cols])

exceeds = []
for i, diff in enumerate(diffs):
    if len(sys.argv) > 3:
        threshold = 0.01 if sys.argv[3] == "percent" else sys.argv[3] if check_float(sys.argv[3]) else 10
        diff = diff/data_set1*100 if sys.argv[3] == "percent" else diff
    else:
        threshold = 10
    if (np.abs(diff) >= threshold).any():
        exceeds.append(i)
[print(f'Column {i} has differences exceeding threshold {threshold}') for i in exceeds]
        
