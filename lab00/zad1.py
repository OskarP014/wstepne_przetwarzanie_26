import numpy as np
import pandas as pd

wartosci = range(1,101)

indexy = [f'ena_{str(i).zfill(3)}' for i in range(1,101)]

seria = pd.Series(wartosci, index=indexy)
print(seria)
