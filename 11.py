import pandas as pd

file = open("./NISPUF17.csv")
df = pd.read_csv(file, sep=',', encoding='utf-8')

len = len(df['SEX'])


df['SEX'] = df['SEX'].replace([1, 2], ['Male', 'Famale'])
df['HAD_CPOX'] = df['HAD_CPOX'].replace([1, 2, 77], ['yes', 'no', 'None'])
df = df.rename(columns={'SEX': 'sex', 'P_NUMVRC': 'Count of dose', 'HAD_CPOX': 'Contracted'})


df = df.drop(df[df['Count of dose'] < 1].index)
df = df.drop(df[df['Contracted'] != 'yes'].index)
df = df.dropna(subset=['Count of dose', 'Contracted'])



sex = list(df['sex'].value_counts())
res = [round(sex[0]/len, 4), round(sex[1]/len, 4)]

print('{"male": ', {res[0]}, f'\n', '"female": ', {res[1]}, '}', sep='')