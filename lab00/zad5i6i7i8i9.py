import numpy as np
import pandas as pd

iris = pd.read_csv('iris.data')

print(iris.head())

iris.columns = iris.columns.str.replace(' ', '_')
print(iris.head(10))

print("Zużycie pamięci deep=False:\n", iris.memory_usage(deep=False).sum())
print("\nZużycie pamięci deep=True:\n", iris.memory_usage(deep=True).sum())

iris_smaller = iris.copy()
float_cols = iris_smaller.select_dtypes(include=['float64']).columns
iris_smaller[float_cols] = iris_smaller[float_cols].astype('float32')

print("\nZużycie pamięci po rzutowaniu na float32 deep=True:\n", iris_smaller.memory_usage(deep=True).sum())

iris.to_clipboard()

nowa_ramka = pd.read_clipboard()
print(nowa_ramka.head(5))

iris.to_parquet('iris.parquet')

iris.to_json('iris.json')

iris.to_pickle('iris.pkl')