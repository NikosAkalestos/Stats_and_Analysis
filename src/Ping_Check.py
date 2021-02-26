import sys

import matplotlib.pyplot as plt
import pandas as pd
from pip._vendor import requests

base_url = "https://api.binance.com"
end_time = "/api/v3/time"
response = requests.get(base_url + end_time)
temp = response.text.strip("{\"serverTime\":" + "}")
repeats = 100
total = 0
table = []

for i in range(repeats):
    response = requests.get(base_url + end_time)
    # print(response.text)
    response_edit = response.text.strip("{\"serverTime\":" + "}")
    # print(response_edit)
    table.append(int(response_edit) - int(temp))
    # print(table[i])
    total = total + table[i]
    temp = response_edit
print("Average latency of \'" + str(repeats) + "\' pings " + str(total / repeats))
df = pd.DataFrame(table)
df.plot()  # plot
plt.show()
sys.exit()

