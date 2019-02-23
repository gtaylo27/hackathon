import numpy as np
import pandas as pd


data = np.genfromtxt(open("entry_exit/entry_exit.csv", "r"), delimiter=",", skip_header=1)

df = pd.read_csv("entry_exit/entry_exit.csv")
client_id = df.client_id

print(client_id.shape)

appeared_ids
for id in client_id:
     is id in appeared_ids
    