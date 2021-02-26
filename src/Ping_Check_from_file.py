import sys

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Shini\Desktop\IdeaProjects\Computer_Aided_Trading\Java_pingCheck_100.csv", header=None)
# df = df.replace(0, np.NaN)
print(df)
print("Average ping of 100 checks is: " + str(float(df[[0]].mean())))
df.plot()  # plot
plt.savefig('..\pings.png', dpi=1080)
plt.show()
sys.exit()
