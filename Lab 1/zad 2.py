import pandas
import numpy as np


df = pandas.DataFrame({'name': ['Antek', 'Maciek', 'Michał', 'Kuba', 'Marian'],
                       'surname': ['Nowak', 'Kocon', 'Kowalczyk', 'Ziemia', 'Zielony'],
                       'sex': ['Male', 'Male', 'Male', 'Male', 'Male']})
print(df.info, df.describe(), df.head(3))

