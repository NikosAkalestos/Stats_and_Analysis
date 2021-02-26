import re
import sys

import pandas as pd
from time import sleep
import time
from datetime import datetime
import matplotlib.pyplot as plt

from pip._vendor import requests

base_url = "https://api.binance.com"
end_ticker_all = "/api/v3/ticker/price"
millis_of_01m = 60000

#todo use pd.read_json
def clean_response(response):
    response = response.replace("[", "")
    response = response.replace("]", "")
    response = response.replace("{\"", "")
    response = response.replace("\":\"", "")
    response = response.replace("\",:\"", ",")
    response = response.replace("\"}", "")
    response = response.replace("\",\"", ",")
    response = response.replace("price", "[")
    return response


def header(header):
    header = re.sub(r',\[\d*\.\d*', r'', header)
    header = header.replace("symbol", "")
    header = header.replace("[", "")
    header = 'TIMESTAMP,FULL_TIME,' + header
    return header


def body(body):
    body = re.sub(r'[a-z]+[A-Z0-9]+|[a-z]+[A-Z0-9A-Z]+|[a-z]+[A-Z]+', r'', body)
    body = body.replace(",[", "").replace(",,[", ",")
    timestamp = int(time.time() * 1000)
    full_time = str(datetime.fromtimestamp(timestamp / 1000.0))
    body = str(timestamp) + "," + full_time + "," + body
    return body


response = requests.get(base_url + end_ticker_all)
headers = header(clean_response(response.text))
# filename = r'..\activity-a-0.csv'
for i in range(86400):
    response = requests.get(base_url + end_ticker_all)
    response = clean_response(response.text)
    if i == 0 or headers != header(response):
        headers = header(response)
        t = str(datetime.fromtimestamp(int(time.time())))
        t = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')#.%f
        t = t.strftime('%I%p %d-%m-%Y')  # save by hour
        filename = r'..\activity '+str(t)+'.csv'
        original_df = pd.DataFrame([body(response).split(",")], columns=headers.split(","))
        original_df.to_csv(filename, header=True, index=False, sep=',', mode='a')
        continue
    original_df = original_df.append(pd.DataFrame([body(response).split(",")], columns=headers.split(",")),
                                     ignore_index=True, sort=False)
    original_df.tail(1).to_csv(filename, header=False, index=False, sep=',', mode='a')
    percentage = i / 86400 * 100
    print(str("%.3f /100") % percentage)
    sleep(1)
print("\'COMPLETED\'")
sys.exit()

