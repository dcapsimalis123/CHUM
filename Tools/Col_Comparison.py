import numpy as np
import pandas as pd
import matplotlib.pyplot as pd
import sys


data_set1 = pd.readcsv(sys.argv[1])
data_set2 = pd.readcsv(sys.argv[2])

data_set1 = np.array(data_set1)
data_set2 = np.array(data_set2)

if np.shape(data_set1) != np.shape(data_set2):
    if len(sys.argv) <= 4:
        print('Data Sets of differing shape')
        exit()

# calc the basic amount of all diffs for either all columns or a selection of columns
if len(sys.argv) <= 4:
    cols = np.range(len(data_set1))
else:
    cols = sys.argv[4:]

diffs = np.array([data_set1[i] - data_set2[i] for i in cols])


for diff in diffs:
    threshold = 0.01      if sys.argv[3] == "percent" else threshold = 1 if sys.argv[3] == "absolute" else sys.argv[3]
    diff = diff/data_set1 if sys.argv[3] == "percent" else diff
    if diff >= threshold:
        print(diff)
