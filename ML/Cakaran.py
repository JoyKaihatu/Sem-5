import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = pd.Series([7,7,6,8,5,3,0], index=['adi','budi','cyntia','denis','erwin','turqon','ginda'])
print(sum(a['adi':'denis']))