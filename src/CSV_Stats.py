import sys

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.vector_ar.vecm import coint_johansen

df = pd.DataFrame(pd.read_csv(r"..\activity 01PM 03-01-2021.csv", header=0))


# defs
def corr_any_pair_with_top_coins(df, pair, byHour, plots):
    top_pairs = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']

    def pair_table(df, pairs):
        for top_pair in top_pairs:
            print()
            for pair in pairs:
                corr = df[top_pair].corr(df[pair])
                print("Correlation for " + pair + " and " + top_pair + " is:\t" + str(corr))
                #todo test Cointegration for non stationary timelines
                # coint = ts.coint(df[top_pair], df[pair])
                # print("Cointergration for " + pair + " and " + top_pair + " is:\t" + str(coint))
                df1 = df[[top_pair]] / df[[top_pair]].mean()
                df2 = df[[pair]] / df[[pair]].mean()
                if float(df1.mean()) > float(df2.mean()):
                    try:
                        df1 = df1 * (float(df2.mean()) / float(df1.mean()))
                    except ZeroDivisionError:
                        continue
                else:
                    try:
                        df2 = df2 * (float(df1.mean()) / float(df2.mean()))
                    except ZeroDivisionError:
                        continue
                if plots:
                    ax = df1.plot(color="black")
                    df2.plot(color="red", ax=ax)
                    plt.show()

    def corr_by_hour(df, pairs):
        def loop(start, end):
            for pair in pairs:
                print()
                for top_pair in top_pairs:
                    corr = df[top_pair][start:end].corr(df[pair][start:end])
                    print("Correlation from: " + str(df["FULL_TIME"][end]) +
                          " to " + str(df["FULL_TIME"][start]) + " for " + pair + " and " +
                          top_pair + " is:\t" + str(corr))
                    df1 = df[top_pair][start:end] / df[top_pair][start:end].mean()
                    df2 = df[pair][start:end] / df[pair][start:end].mean()
                    if float(df1.mean()) > float(df2.mean()):
                        # if df1.mean() > df2.mean():
                        try:
                            df1 = df1 * (float(df2.mean()) / float(df1.mean()))
                        except ZeroDivisionError:
                            continue
                        else:
                            try:
                                df2 = df2 * (float(df1.mean()) / float(df2.mean()))
                            except ZeroDivisionError:
                                continue
                    if plots:
                        ax = df1.plot(color="black")
                        df2.plot(color="red", ax=ax)
                        plt.show()

        x = (int(df["TIMESTAMP"].tail(1)))
        x = x - 3600000
        end = len(df) - 1
        if x < (int(df["TIMESTAMP"].head(1))):
            loop(0, end)
            return
        for i in range(end, 0, -1):
            if x > df["TIMESTAMP"][i] or i == 0:
                loop(i, end)
                end = i
                x = (int(df["TIMESTAMP"][i]))
                x = x - 3600000
                print("\n\t\t\tLAST HOUR")

    """    todo/sorting/new df/etc/lose bad pairs
    def pair_table(df, pairs):
        for top_pair in top_pairs:
            for pair in pairs:
                corr = df[top_pair].corr(df[pair])
                print("Correlation for " + top_pair + " and " + pair + " is:\t" + str(corr))
                df1 = df[[top_pair]] - df[[top_pair]].mean()
                df2 = df[[pair]] - df[[pair]].mean()
                if float(df1.mean()) > float(df2.mean()):
                    try:
                        df1 = df1 * (float(df2.mean()) / float(df1.mean()))
                    except ZeroDivisionError:
                        continue
                else:
                    try:
                        df2 = df2 * (float(df1.mean()) / float(df2.mean()))
                    except ZeroDivisionError:
                        continue
                # ax = df1.plot(color="black")
                # df2.plot(color="red", ax=ax)
                # plt.show()
    """

    if byHour:
        corr_by_hour(df, pair)
        return
    else:
        if pair == "all" or pair == "ALL":
            pair = df.columns[2:]
            pair_table(df, pair)
            return
        pair_table(df, pair)


def corr_all(df):
    df_corr = df.corr()
    print(df_corr.to_string())


# corr_all(df)

# disable stats by hour if false # disabled plots if FALSE
corr_any_pair_with_top_coins(df, ['ETHUSDT', 'LINKUSDT', 'BNBUSDT', 'SUSHIUSDT', 'YFIUSDT', 'YFIIUSDT'], False, True)
sys.exit()

"""
def corr_by_hour(df, pair):
 x = (int(df["TIMESTAMP"].tail(1)))
 x = x - 3600000
 for i in range(len(df) - 1, 0, -1):
     if x > df["TIMESTAMP"][i]:
         break

 corr = df["BTCUSDT"][i:len(df)].corr(df["SUSHIUSDT"][i:len(df)])

 print("Correlation from:\t" + str(df["FULL_TIME"][i]) +
       " to \t" + str(df["FULL_TIME"][len(df) - 1]) + " for BTC and SUSHI:\t" + str(corr))

 print(x)

 print("BNBUSDT,SUSHIUSDT,YFIUSDT,YFIIUSDT".split(","))
 corr_any_pair_with_top_coins(df, "all") #runs out of memory, needs sorting and to lose the unused currencies

 """
