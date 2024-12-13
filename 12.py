import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('./Mall_Customers.csv')


res1 = df.groupby("Genre").mean('Annual Income (k$)')
print(f'Средняя доходность женщин: {round(list(res1['Annual Income (k$)'])[0], 2)}')



res2 = pd.DataFrame()
res2['Spending Score (1-100)'] = (df.groupby('Genre')['Spending Score (1-100)'].max())
res2['CustomerID'] = df.groupby('Genre')[['Spending Score (1-100)']].idxmax()+1
print(res2)



graf = df.drop(df[df['Genre'] != 'Male'].index)
graf = graf.groupby('Age')[['Annual Income (k$)']].mean()

res3 = graf.plot(title='Male salary based on age', xlabel='Age', ylabel='Annual Income (k$)', grid=True, colormap='rainbow', legend = 'False')
plt.show()



graf2 = df[['Genre', 'Spending Score (1-100)', 'Annual Income (k$)']]
graf3 = graf2.drop(df[df['Genre'] != 'Male'].index)
graf4 = graf2.drop(df[df['Genre'] != 'Female'].index)

plt.bar(graf3['Spending Score (1-100)'], graf3['Annual Income (k$)'], color = 'red', label='Male')
plt.bar(graf4['Spending Score (1-100)'], graf4['Annual Income (k$)'], color = 'blue', label = "Female")
plt.xlabel('Spending Score (1-100)')
plt.ylabel('Annual Income (k$)')
plt.grid('True')
plt.legend(loc='upper right')

plt.show()