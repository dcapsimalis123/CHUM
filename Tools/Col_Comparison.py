import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


data_set1 = pd.read_csv(sys.argv[1])
data_set2 = pd.read_csv(sys.argv[2])

data_set1 = np.array(data_set1)
data_set2 = np.array(data_set2)

if np.shape(data_set1) != np.shape(data_set2):
    if len(sys.argv) <= 4:
        print('Data Sets of differing shape')
        quit()

# calc the basic amount of all diffs for either all columns or a selection of columns
if len(sys.argv) <= 4:
    cols = range(data_set1.shape[0])
else:
    cols = sys.argv[4:]

diffs = np.array([data_set1[i] - data_set2[i] for i in cols])

def check_actual_type(val: str):
    try:
        float(val)
        return True
    except ValueError:
        return False

exceeds = []
for i, diff in enumerate(diffs):
    if len(sys.argv) > 3:
        threshold = 0.01 if sys.argv[3] == "percent" else sys.argv[3] if check_actual_type(sys.argv[3]) else 10
        diff = diff/data_set1*100 if sys.argv[3] == "percent" else diff
    else:
        threshold = 10
    if (np.abs(diff) >= threshold).any():
        exceeds.append(i)
[print(f'Column {i} has differences exceeding threshold {threshold}') for i in exceeds]
        
