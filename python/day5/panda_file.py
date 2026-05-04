import pandas as pd

la_def=pd.read_csv('day5\Superstore sales dataset.csv')

#print(la_def.head())

#print(la_def.tail())

#print(la_def.info())

new_df=la_def.dropna()



print(la_def.duplicated())
