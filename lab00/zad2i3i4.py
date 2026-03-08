import numpy as np
import pandas as pd

bases = np.arange(1, 11)
powers = np.arange(1, 11)

arr = bases[:, None] ** powers

kolumny = ['base'] + [f'pow_{i}' for i in range(2, 11)]

df = pd.DataFrame(arr, columns=kolumny)
print(df)

print("Czy oryginalna ramka dzieli pamięć z arr?", np.shares_memory(arr, df))

df_shared = pd.DataFrame(arr, columns=kolumny, copy=False)
print("Czy nowa ramka dzieli pamięć z arr?", np.shares_memory(arr, df_shared))

print("Typy przed downcastem:\n", df_shared.dtypes)

df_downcast = df_shared.apply(pd.to_numeric, downcast='integer')
print("\nTypy po downcaście:\n", df_downcast.dtypes)