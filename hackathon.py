import numpy as np

data = np.genfromtxt(open("entry_exit/entry_exit.csv", "r"), delimiter=",", skip_header=1)

print(data.shape)