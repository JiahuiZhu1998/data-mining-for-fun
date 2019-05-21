import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

#%matplotlib inlines
print('Python version'+sys.version)
print('Pandas version'+pd.__version__)
print('Matplotlib version' + matplotlib.__version__)

## set numpy seed
np.seed(111)

def createDataSet(Number=1):
    output = []
