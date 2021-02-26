import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

x = np.arange(1, 1.07, 0.0001)

# basic = 0.988
basic2 = 1 / (((x - 1) * 0.3) + 1)
f_basic = 1 / (((5 * (x - 1)) / (x ** 10)) + 1)

# small amplitude
t = 1 / (((0.01 + (x - 1)) / (x ** 12) + 0.03) + 1)
try_4_0 = (1 / ((((x - 1)) / (10 * (x ** 3)) + 0.01) + 1))
try_4_1 = ((1 / ((((x - 1)) / (10 * x ** 3) + 0.01) + 1)) + 0.00235)
try_4_2 = ((1 / ((((x - 1)) / (10 * x ** 3) + 0.01) + 1)) + 0.00235) * 1.002104419

try_4_3 = 1 / (((10 * (x - 1)) / (x ** 95)) + 1)
try_4_4 = 1 / (((10 * (x - 1)) / (x ** 80)) + 1)


def corrs():
    y = np.arange(1.0000001, 20, 0.01)
    t5 = ((1 / ((((y - 1)) / (10 * y ** 3) + 0.01) + 1)) + 0.00235) * 1.002104419
    df1 = pd.DataFrame(try_4_0)
    df2 = pd.DataFrame(t5)
    # pd.to_numeric(df1)
    # pd.to_numeric(df2)
    print("Corr is:\t" + str(df2[0].corr(df1[0])))
    plt.plot(df1[0], color="red")
    plt.plot(df2[0], color="black")
    plt.show()
    # corr = df1.corr(df2)
    # print(corr)


# corrs()


def plots():
    # plt.xticks()
    # plt.subplot.set_xlim([1.0000001, 2])
    # plt.xlim(left=1)
    # plt.xlim(1, 4, 0.01)
    # plt.ylim(0.85, 1, 0.0005)
    # plt.plot(basic, color="red")
    # plt.plot(basic, color="green")
    #
    # print((1 / ((((1 / 0.988) - 1) * 2) + 1.0016)))
    plt.axhline(y=(1 / ((((1 / 0.988) - 1) * 2) + 1.0016)), color='green', linestyle='-')
    plt.axhline(y=0.988, color='green', linestyle='-')
    plt.axhline(y=0.994, color='green', linestyle='-')
    # plt.plot(t, color="black")
    # plt.plot(t2, color="red")
    # plt.plot(t3, color="grey")
    # plt.plot(t4, color="orange")
    plt.plot(try_4_3, color="black")
    plt.plot(try_4_4, color="red")

    plt.plot(f_basic, color="blue")

    plt.grid()
    plt.savefig('..\plots.png', dpi=1080)
    plt.show()


plots()


def calculator():
    x_temp = 1.06810459
    change_temp = 1.006185958
    t2_temp = (1 / (((x_temp - 1) / (10 * x_temp ** 3) + 0.01) + 1)) + 0.00235
    print("\nStop Loss is:\t" + str(t2_temp) + "\nChange was:\t\t" + str(
        change_temp / x_temp) + "\n\nNet Amplitude is:\t" + str(x_temp) + "\nFinal % is:\t\t\t" + str(x_temp * t2_temp))


# calculator()


def prices():
    x = 1
    y = 0.00352
    holder = y * 0.988
    min = y * 0.988
    y = min
    print(holder, min, y)
    for i in range(1, 1000, 1):
        y = y + 0.000001
        x = y / min
        # f_basic = 1 / (((5 * (x - 1)) / (x ** 10)) + 1)
        # t2 = (1 / ((((x - 1)) / (10 * x ** 3) + 0.01) + 1)) + 0.00235
        t2 = 1 / (((10 * (x - 1)) / (x ** 80)) + 1)
        flag = (t2 * y) > holder
        flag2 = y > (min * ((1 / 0.988) + 0.0015))
        print(str(x) + "\t" + str(y) + "\t" + str(y * t2) + "\t" + str(holder) + "\t" + str(t2) + "\t" + str(
            flag) + "\t" + str(flag2))
        if flag:
            holder = t2 * y


# prices()

def percentages():
    x_temp = 1
    for i in range(1, 2000, 1):
        x_temp += 0.0001
        t6 = 1 / (((10 * (x_temp - 1)) / (x_temp ** 95)) + 1)
        t7 = 1 / (((10 * (x_temp - 1)) / (x_temp ** 80)) + 1)
        print(str(x_temp) + "\t" + str(t6) + "\t" + str(t7))


percentages()
sys.exit()
