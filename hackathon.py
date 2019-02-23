import numpy as np

data = np.genfromtxt(open("services/client.csv", "r"), delimiter=",", skip_header=1)

print(data.shape)