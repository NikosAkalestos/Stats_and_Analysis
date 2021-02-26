import sys
import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pip._vendor import requests

# todo scan by day if less than 24 values delete the day and move to the next one
##
now = int(time.time() * 1000)
millis_of_01m = 60000
millis_of_01H = 3600000
millis_of_24H = 86400000
millis_of_30D = 2592000000
millis_of_41D = 3542400000

##
base_url = "https://api.binance.com"
end_klines = "/api/v3/klines"
symbol = "BTCUSDT"
interval = "1h"
startTime = now - millis_of_24H * 10
endTime = now  # + millis_of_24H  # startTime + millis_of_41D  # 36 * millis_of_01H
# full_limit = 984
limit = 24 * 1 * 10

if startTime <= now - 10:
    response = requests.get(
        base_url + end_klines + "?symbol=" + symbol + "&interval=" + interval + "&startTime=" + str(
            startTime) + "&limit=" + str(limit))
if endTime <= now - 10:
    response = requests.get(
        base_url + end_klines + "?symbol=" + symbol + "&interval=" + interval + "&startTime=" + str(
            startTime) + "&endTime=" + str(endTime) + "&limit=" + str(limit))

# clean
# todo use pd.read_json
x = response.text
x = x.replace("[", "", 2)
x = x.replace("]", "")
x = x.replace(",[", ",")
x = x.replace("\"", "")
# reshape

x1 = np.array(x.split(","))
# print(x1[:][0:12])

x1 = x1.reshape(limit, 12)
original_df = pd.DataFrame(x1)
test_df = pd.DataFrame(x1)
t = []

for i in range(limit):
    t = str(datetime.fromtimestamp(int(test_df[0][i]) / 1000.0))
    t = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')  # save by hour
    t = t.strftime('%H')  # save by hour
    test_df[0][i] = t  # save by hour

new_df = test_df[[0, 5]].copy()
new_df[0] = pd.to_numeric(new_df[0])
new_df[5] = pd.to_numeric(new_df[5])
# print(new_df.groupby(0).mean())
# print(new_df.groupby(0).sum())

t1 = new_df.groupby(0).mean()
t1.plot()
# plt.xlim(1, 24, 1)
plt.grid()
plt.savefig('..\Hour_Activity.png', dpi=1080)
plt.show()
sys.exit()

# df.to_csv(r'activity.txt', header=None, index=True, sep=',', mode='a')

# header=[True,list["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume","Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"]], index=True, sep=',', mode='a')

#
# df.plot(x=df[0], y=df[5], kind='scatter')
# plt.show()
# print(df[0])
# original_stdout = sys.stdout  # Save a reference to the original standard output

# with open('python_Data.txt', 'a') as f:
#
#     sys.stdout = f  # Change the standard output to the file we created.
#     print(df)
#     sys.stdout = original_stdout  # Reset the standard output to its original value
#
# """
