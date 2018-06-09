import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df =   pd.read_csv('data\SET.TXT')

df['Date'] = pd.to_datetime(df.Date, format='%Y%m%d')
df.set_index('Date', inplace=True)

dfFilter = df[df > 1000]
ax = dfFilter.loc[:,['Close']].plot(color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('The values of my Y axis')

ax.set_title('SET index')
plt.show()