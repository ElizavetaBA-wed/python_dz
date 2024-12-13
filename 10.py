#1

import pandas as pd
fruits= ["apple", "pear", "orange", "tangerine", "banana", "kiwi", "peach", "plum", "grape", "pineapple"]
fruits_series = pd.Series(fruits)
print(fruits_series)

#2

import pandas as pd
df= pd.DataFrame({
    'fruits_1': ["apple", "pear", "orange", "tangerine", "banana"],
    'fruits_2': [ "tangerine", "banana", "kiwi", "peach", "plum"]})
print(df)
print( df[df != df.loc[df['fruits_1'].isin(df['fruits_2']), 'fruits_1'].values].dropna())

#3

import pandas as pd
from matplotlib import pyplot as plt

sr= pd.Series(["orange","orange","orange","orange","orange", "tangerine", "banana", "tangerine", "banana", "tangerine", "banana", "tangerine", "tangerine", "tangerine", "tangerine"])
print(sr)

plt.bar(sr.value_counts().index, sr.value_counts().values)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
