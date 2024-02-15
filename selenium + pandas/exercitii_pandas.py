import pandas as pd
import numpy as np

# dintr-o lista
#lista = [10, 20, 30, 40, 50]
#etichete = ['a', 'b', 'c', 'd', 'e']
#serie = pd.Series(lista, index = etichete)
#serie = pd.Series(lista)
#print(serie[ ['a', 'c', 'd'] ])

#dintr-un array numpy
array_date = np.array([10, 20, 30, 40, 50])
serie = pd.Series(array_date)
print(serie)

#dintr-un dictionar
#dict_date = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e':50}
#serie = pd.Series(dict_date)
#print(serie)

# SERIA E O COLOANA DINTR-UN DATAFRAME!!!!!
data = {"nume": ["ana", "bogdan", "cristina"],
        "varsta": [25,30,22],
        "salariu":[50000, 60000, 45000]}
df = pd.DataFrame(data)
df['Experienta'] = [2,5,1]
#print(df)
#df.set_index('nume', inplace = True)
#print(df)
#print(df.loc['bogdan'])
df.to_csv('nou.csv')